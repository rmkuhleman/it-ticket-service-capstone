# IT Ticket Service Workflow

This workflow explains how a user submits a ticket, what the system does in terms of organization and storage, how the ticket is reviewed and updated by a technician, and how the user provides feedback after the issue is resolved. This further defines the full process of the IT Ticket Service.

## Main Actors

- **User:** Submits a ticket and gives feedback following the issue’s resolution.
- **System:** Stores the ticket, organizes it, and supports routing or escalation.
- **Technician/Admin:** Reviews tickets, updates ticket statuses, resolves issues, or escalates them when needed.

## Workflow Steps

1. The user logins the IT Ticket Service form.
3. The user enters required information such as name, email, username, phone number, machine ID/name, issue category, issue subcategory, and a brief description of the issue.
4. The user submits the ticket into the system.
5. The system stores the ticket and gives it a default status of **Open**.
6. The system oragnize tickets to allow the use of filters for the user and the technician/admin.
7. A technician or admin views the submitted ticket in the dashboard.
8. The technician or admin reviews the contents of the ticket and updates the ticket status when needed.
9. If the issue is more serious or requires a higher level of support, the ticket is escalated.
10. If the issue can be handled without escalation, the technician or admin works toward resolving the issue.
11. Once the issue is resolved, the ticket status is changed to **Closed**.
12. The user is informed that the ticket has been closed.
13. The user submits feedback about the service.

## Ticket Status Flow

A ticket will usually move through the following statuses:

**Open → In Progress → Closed**

If a more serious issue occurs, the flow may become:

**Open → In Progress → Escalated → Closed**
