# IT Ticket Service Technology Stack

This document explains the technology stack used for the IT Ticket Service project and why each component was chosen. The goal was to use tools that are practical, efficient, and appropriate for the scope of this capstone project.


## Backend
The backend of the project uses **Python with Flask**.

### Reason for Choice
Python is a widely used and practical programming language for building web applications. Flask is a lightweight web framework that allows for quick development while supporting routing, form handling, session management, and database interaction. It was chosen to keep the project simple while still enabling full backend functionality.


## Frontend
The frontend of the project uses **HTML, CSS, and JavaScript**.

### Reason for Choice
These technologies provide everything needed to build a clean and functional user interface. HTML structures the pages, CSS handles styling and layout, and JavaScript enables dynamic behavior such as time formatting and interactivity. This approach keeps the project manageable while still delivering a good user experience.


## Database
The database for the project uses **SQLite**.

### Reason for Choice
SQLite is a lightweight, file-based database that does not require a separate server. It is ideal for small to medium-sized applications and allows for quick setup and easy data management. It is used to store users, tickets, and feedback data.


## Development Tools
The project was developed using:

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- GitHub (version control and documentation)


## Key Technical Features

- Session-based authentication
- Password hashing using Werkzeug
- Role-based access control (user vs admin)
- Relational database design (tickets, users, feedback)
- Form validation and input sanitization
- Dynamic status handling (Open, In Progress, Escalated, Closed)


## Project Structure

```text
it-ticket-service-capstone/
├── app.py
├── tickets.db
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── my_tickets.html
│   ├── confirm.html
│   ├── tickets.html
│   └── feedback.html
|   └── ticket_details.html
├── static/
│   ├── style.css
│   └── script.js
├── docs/
│   ├── project-scope.md
│   ├── workflow-diagram.md
│   ├── page-plan.md
│   ├── technology-stack.md
│   ├── development-log.md
│   ├── time-log.md
│   └── testing-notes.md
├── images/
└── README.md
