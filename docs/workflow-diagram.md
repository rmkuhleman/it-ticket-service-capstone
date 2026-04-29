# IT Ticket Service Workflow

This workflow explains how a user submits a ticket, how the system processes and stores it, how an administrator manages the ticket, and how feedback is collected after resolution. It represents the complete lifecycle of a ticket within the IT Ticket Service.

---

## Main Actors

- **User:** Logs in, submits tickets, tracks status, and provides feedback after resolution.  
- **System:** Stores tickets, manages sessions, enforces access control, and supports filtering and organization.  
- **Technician/Admin:** Reviews tickets, updates statuses, adds resolution notes, escalates issues, and closes tickets.  

---

## Workflow Steps

1. The user logs into the IT Ticket Service using a username and password.  
2. If the user does not already have an account, one is created automatically.  
3. The user submits a ticket by entering required information such as name, contact details, machine ID, issue category, and description.  
4. The system validates the input and stores the ticket in the database.  
5. The ticket is assigned a default status of **Open**.  
6. The user can view their ticket on the **My Tickets** dashboard, with filtering and status tracking.  
7. An administrator logs in and accesses the **Admin Dashboard** to view all tickets.  
8. The administrator reviews the ticket and updates its status as needed.  
9. If the issue requires higher-level support, the ticket is marked as **Escalated**.  
10. If the issue can be handled directly, the administrator continues working on it and may mark it as **In Progress**.  
11. Once the issue is fully resolved, the administrator updates the ticket status to **Closed** and may add resolution notes.  
12. The user can view the updated ticket details, including resolution notes once the ticket is closed.  
13. The user submits feedback (rating and comments) for the resolved ticket.  

---

## Ticket Status Flow

A ticket progresses through the following lifecycle:

**Open → In Progress → Escalated → Closed**

Notes:
- **Escalated** indicates the issue requires higher-level support and is still active.  
- **Closed** indicates the issue has been fully resolved.  
- Feedback is only available once a ticket is closed.  

---

## Access Control

- Users can only view and interact with their own tickets.  
- Administrators have access to all tickets and management functionality.  
- Role-based access control ensures separation between user and admin actions.  
