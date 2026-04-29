from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import re
import sqlite3
from datetime import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_key"

VALID_STATUSES = {"open", "in progress", "escalated", "closed"}
INACTIVITY_TIMEOUT_SECONDS = 30 * 60


def normalize_status(status):
    status = (status or "open").strip().lower()
    return status if status in VALID_STATUSES else "open"


def get_db_connection():
    conn = sqlite3.connect("tickets.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email TEXT,
            phone TEXT,
            username TEXT,
            machine_id TEXT,
            category TEXT,
            subcategory TEXT,
            description TEXT,
            status TEXT DEFAULT 'open',
            created_at TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS technicians (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            rating INTEGER NOT NULL,
            comments TEXT,
            created_at TEXT,
            FOREIGN KEY (ticket_id) REFERENCES tickets(id)
        )
    """)

    existing_cols = conn.execute("PRAGMA table_info(tickets)").fetchall()
    existing_col_names = {col["name"] for col in existing_cols}

    if "resolution_notes" not in existing_col_names:
        conn.execute("ALTER TABLE tickets ADD COLUMN resolution_notes TEXT")
    if "escalation_level" not in existing_col_names:
        conn.execute("ALTER TABLE tickets ADD COLUMN escalation_level TEXT DEFAULT 'none'")
    if "assigned_to" not in existing_col_names:
        conn.execute("ALTER TABLE tickets ADD COLUMN assigned_to INTEGER")

    existing_user_cols = conn.execute("PRAGMA table_info(users)").fetchall()
    existing_user_col_names = {col["name"] for col in existing_user_cols}

    if "role" not in existing_user_col_names:
        conn.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")

    conn.commit()
    conn.close()


init_db()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            return redirect(url_for("my_tickets"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        if session.get("role") == "admin":
            return redirect(url_for("tickets"))
        return redirect(url_for("my_tickets"))

    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")

        if not username or not password:
            error = "Username and password are required."
            return render_template("login.html", error=error)

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        if user:
            if not check_password_hash(user["password_hash"], password):
                conn.close()
                error = "Invalid username or password."
                return render_template("login.html", error=error)
            role = user["role"] or "user"

        else:
            password_hash = generate_password_hash(password)
            role = "user"

            conn.execute(
                """
                INSERT INTO users (username, password_hash, role, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (username, password_hash, role, datetime.now().isoformat())
            )
            conn.commit()

        conn.close()

        session["username"] = username
        session["role"] = role
        session.permanent = False
        session["last_active"] = datetime.now().timestamp()

        if session.get("role") == "admin":
            return redirect(url_for("tickets"))

        return redirect(url_for("my_tickets"))

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("role", None)
    session.pop("last_active", None)
    return redirect(url_for("login"))


@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    username = session.get("username")

    conn = get_db_connection()
    has_tickets = conn.execute(
        "SELECT COUNT(*) FROM tickets WHERE LOWER(username) = ?",
        (username,)
    ).fetchone()[0] > 0
    conn.close()

    if request.method == "POST":
        form_data = {
            "full_name": request.form.get("full_name", "").strip()[:100],
            "email": request.form.get("email", "").strip()[:254],
            "phone": request.form.get("phone", "").strip()[:25],
            "machine_id": request.form.get("machine_id", "").strip()[:100],
            "category": request.form.get("category", "").strip(),
            "subcategory": request.form.get("subcategory", "").strip(),
            "description": request.form.get("description", "").strip()[:3000]
        }

        errors = []
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not form_data["full_name"]:
            errors.append({"field": "full_name", "message": "Full name is required"})
        if not form_data["email"] and not form_data["phone"]:
            errors.append({"field": "contact", "message": "Provide at least one contact method (email or phone)"})
        if form_data["email"] and not re.match(email_pattern, form_data["email"]):
            errors.append({"field": "email", "message": "Enter a valid email address"})
        if form_data["phone"] and not form_data["phone"].replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("+", "").isdigit():
            errors.append({"field": "phone", "message": "Enter a valid phone number"})
        if not form_data["category"]:
            errors.append({"field": "category", "message": "Issue category is required"})
        if not form_data["description"]:
            errors.append({"field": "description", "message": "Description is required"})

        if errors:
            session["errors"] = errors
            session["form_data"] = form_data
            session.modified = True
            return redirect(url_for("home"))

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO tickets (
                full_name, email, phone, username,
                machine_id, category, subcategory, description, status, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            form_data["full_name"], form_data["email"], form_data["phone"], username,
            form_data["machine_id"], form_data["category"], form_data["subcategory"],
            form_data["description"], normalize_status("open"), datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()

        session.pop("form_data", None)
        session.pop("errors", None)

        return redirect(url_for("my_tickets"))

    errors = session.get("errors", [])
    form_data = session.get("form_data", {})

    return render_template(
        "index.html",
        errors=errors,
        form_data=form_data,
        username=username,
        has_tickets=has_tickets,
        inactivity_timeout=INACTIVITY_TIMEOUT_SECONDS
    )


@app.route("/my_tickets")
@login_required
def my_tickets():
    username = session.get("username")

    conn = get_db_connection()
    tickets = conn.execute(
        "SELECT * FROM tickets WHERE LOWER(username) = ? ORDER BY created_at DESC",
        (username,)
    ).fetchall()
    conn.close()

    return render_template(
        "my_tickets.html",
        tickets=tickets,
        ticket_id_filter=request.args.get("ticketId", ""),
        category_filter=request.args.get("category", ""),
        subcategory_filter=request.args.get("subcategory", ""),
        description_filter=request.args.get("description", ""),
        date_filter=request.args.get("date", ""),
        inactivity_timeout=INACTIVITY_TIMEOUT_SECONDS
    )


@app.route("/ticket_details")
@login_required
def ticket_details():
    ticket_id = request.args.get("ticket_id", type=int)
    username = session.get("username")

    if not ticket_id:
        return redirect(url_for("my_tickets"))

    conn = get_db_connection()
    ticket = conn.execute(
        "SELECT * FROM tickets WHERE id = ? AND LOWER(username) = ?",
        (ticket_id, username)
    ).fetchone()

    feedback = conn.execute(
        "SELECT * FROM feedback WHERE ticket_id = ? AND LOWER(username) = ?",
        (ticket_id, username)
    ).fetchone()

    conn.close()

    if not ticket:
        return redirect(url_for("my_tickets"))

    return render_template(
        "confirm.html",
        full_name=ticket["full_name"],
        email=ticket["email"],
        phone=ticket["phone"],
        username=ticket["username"],
        machine_id=ticket["machine_id"],
        category=ticket["category"],
        subcategory=ticket["subcategory"],
        description=ticket["description"],
        status=ticket["status"],
        resolution_notes=ticket["resolution_notes"],
        created_at=ticket["created_at"],
        username_param=username,
        inactivity_timeout=INACTIVITY_TIMEOUT_SECONDS,
        feedback_submitted=feedback is not None,
    )


@app.route("/tickets")
@login_required
@admin_required
def tickets():
    search = request.args.get("search", "").strip().lower()
    status_filter = request.args.get("status", "all").strip().lower()
    sort = request.args.get("sort", "newest")

    query = """
        SELECT 
            tickets.*,
            feedback.rating AS feedback_rating,
            feedback.comments AS feedback_comments,
            feedback.created_at AS feedback_created_at
        FROM tickets
        LEFT JOIN feedback ON tickets.id = feedback.ticket_id
        WHERE 1=1
    """
    params = []

    if search:
        query += """
            AND (
                LOWER(full_name) LIKE ?
                OR LOWER(email) LIKE ?
                OR LOWER(username) LIKE ?
                OR LOWER(machine_id) LIKE ?
                OR LOWER(description) LIKE ?
            )
        """
        search_value = f"%{search}%"
        params.extend([search_value, search_value, search_value, search_value, search_value])

    if status_filter != "all":
        query += " AND LOWER(status) = ?"
        params.append(status_filter)

    if sort == "oldest":
        query += " ORDER BY tickets.created_at ASC"
    else:
        query += " ORDER BY tickets.created_at DESC"

    conn = get_db_connection()
    tickets = conn.execute(query, params).fetchall()
    conn.close()

    return render_template(
        "tickets.html",
        tickets=tickets,
        search=search,
        status_filter=status_filter,
        sort=sort
    )


@app.route("/tickets/update/<int:ticket_id>", methods=["POST"])
@login_required
@admin_required
def update_ticket_status(ticket_id):
    status = normalize_status(request.form.get("status"))
    resolution_notes = request.form.get("resolution_notes", "").strip()

    conn = get_db_connection()
    conn.execute(
        """
        UPDATE tickets
        SET status = ?, resolution_notes = ?
        WHERE id = ?
        """,
        (status, resolution_notes, ticket_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("tickets"))


@app.route("/tickets/update-bulk", methods=["POST"])
@login_required
@admin_required
def update_tickets_bulk():
    data = request.get_json()
    updates = data.get("updates", [])

    conn = get_db_connection()

    for update in updates:
        ticket_id = update.get("id")
        status = normalize_status(update.get("status"))
        resolution_notes = update.get("resolution_notes", "").strip()

        if ticket_id:
            conn.execute(
                """
                UPDATE tickets
                SET status = ?, resolution_notes = ?
                WHERE id = ?
                """,
                (status, resolution_notes, ticket_id)
            )

    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/feedback/<int:ticket_id>", methods=["GET", "POST"])
@login_required
def feedback(ticket_id):
    username = session.get("username")

    conn = get_db_connection()

    ticket = conn.execute(
        "SELECT * FROM tickets WHERE id = ? AND LOWER(username) = ?",
        (ticket_id, username)
    ).fetchone()

    if not ticket:
        conn.close()
        return redirect(url_for("my_tickets"))

    if normalize_status(ticket["status"]) != "closed":
        conn.close()
        return redirect(url_for("ticket_details", ticket_id=ticket_id))

    existing_feedback = conn.execute(
        "SELECT * FROM feedback WHERE ticket_id = ? AND LOWER(username) = ?",
        (ticket_id, username)
    ).fetchone()

    if request.method == "POST":
        rating = request.form.get("rating", type=int)
        comments = request.form.get("comments", "").strip()[:1000]

        if not rating or rating < 1 or rating > 5:
            conn.close()
            return render_template(
                "feedback.html",
                ticket=ticket,
                existing_feedback=existing_feedback,
                error="Please select a rating between 1 and 5."
            )

        if existing_feedback:
            conn.execute(
                """
                UPDATE feedback
                SET rating = ?, comments = ?, created_at = ?
                WHERE ticket_id = ? AND LOWER(username) = ?
                """,
                (rating, comments, datetime.now().isoformat(), ticket_id, username)
            )
        else:
            conn.execute(
                """
                INSERT INTO feedback (ticket_id, username, rating, comments, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (ticket_id, username, rating, comments, datetime.now().isoformat())
            )

        conn.commit()
        conn.close()

        return redirect(url_for("ticket_details", ticket_id=ticket_id))

    conn.close()

    return render_template(
        "feedback.html",
        ticket=ticket,
        existing_feedback=existing_feedback,
        error=None
    )

if __name__ == "__main__":
    app.run(debug=True)