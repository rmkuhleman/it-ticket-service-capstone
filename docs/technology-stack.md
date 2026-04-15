# IT Ticket Service Technology Stack

This document explains the technology stack that will be used for the IT Ticket Service project and why each part was chosen. The main goal is to use tools that are simple, practical, and manageable for the scope of this capstone project.

## Backend
The backend of the project will use **Python with Flask**.

### Reason for Choice
Python is a widely used programming language that is practical and easy for this type of application. Flask is a lightweight web framework that works well for small to medium-sized projects. It is a good fit for this capstone because it allows the project to stay simple while still supporting forms, routing, database interaction, and page rendering.

## Frontend
The frontend of the project will use **HTML, CSS, and JavaScript**.

### Reason for Choice
HTML, CSS, and JavaScript are enough to build the pages needed for this project. They support form creation, page layout, styling, and basic interactivity. This keeps the project easier to manage while still allowing the interface to be clear and user-friendly.

## Database
The database for the project will use **SQLite**.

### Reason for Choice
SQLite is a lightweight database that works well for smaller projects and prototypes. It does not require a separate database server, which makes it easier to set up and use during development. It is a practical choice for storing ticket data in this capstone project.

## Development Tools
The project will be developed using:
- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- GitHub for version control and documentation

## Planned Project Structure
The project will likely use a structure similar to the following:

```text
it-ticket-service-capstone/
├── app.py
├── database.db
├── templates/
│   ├── index.html
│   ├── confirm.html
│   ├── dashboard.html
│   ├── ticket_detail.html
│   └── feedback.html
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
└── README.md
