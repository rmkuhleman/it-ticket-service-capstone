# IT Ticket Service Page Plan

This document outlines the main pages included in the IT Ticket Service project. The system is designed to be simple, organized, and user-friendly while supporting ticket submission, tracking, management, escalation, resolution, and feedback.


## Page 1: Login Page

### Purpose
This page allows users to log in or create an account to access the system.

### Main Elements
- Username field
- Password field
- Login / Create Account functionality
- Error messages for invalid input

### Notes
User authentication is session-based, and accounts are created automatically on first login.


## Page 2: Ticket Submission Page (Home)

### Purpose
This page allows the user to submit a support ticket for an IT or technical issue.

### Main Elements
- Full name field
- Email field
- Phone number field
- Machine ID/name field
- Issue category dropdown
- Issue subcategory dropdown
- Description text box
- Submit button

### Notes
The username is pulled from the session and is not manually entered. The form includes validation to ensure required fields are completed.


## Page 3: My Tickets Page

### Purpose
This page allows users to view and manage their submitted tickets.

### Main Elements
- List of user-specific tickets
- Ticket ID
- Status badge (Open, In Progress, Escalated, Closed)
- Description preview
- Filtering options (ID, category, description, date)
- Link to ticket details

### Notes
Users can only view their own tickets. The page is designed as a clean dashboard for quick access to ticket information.


## Page 4: Ticket Details Page

### Purpose
This page displays full details of a selected ticket.

### Main Elements
- Full ticket information
- User and contact details
- Machine ID/name
- Category and subcategory
- Description
- Status badge
- Resolution notes (only visible when closed)
- Link back to My Tickets

### Notes
This page provides a read-only detailed view for users. It ensures users only access their own ticket data.


## Page 5: Admin/Technician Dashboard

### Purpose
This page allows administrators to view and manage all submitted tickets.

### Main Elements
- List of all tickets
- Search and filtering options
- Ticket status dropdown (Open, In Progress, Escalated, Closed)
- Resolution notes input
- Bulk update functionality
- Feedback display (rating and comments)

### Notes
This page is restricted to admin users only. It provides full control over ticket lifecycle management.


## Page 6: Feedback Page

### Purpose
This page allows users to submit feedback after a ticket has been resolved.

### Main Elements
- Ticket reference
- Rating (1–5)
- Comment box
- Submit button

### Notes
Feedback can only be submitted for closed tickets. Users can update their feedback if needed.


## Overall Design Notes

The system minimizes the number of pages while keeping functionality organized and easy to navigate. The design prioritizes clarity, usability, and efficient workflows for both users and administrators.
