# Results of the Project

## 1. Original Proposal Background

The original proposal described an IT ticket service that would let users submit technical issues, organize those issues by category, and help determine whether the issue needed regular or higher-level support. The goal was a simple, user-friendly service that could be adapted for organizations that need a faster way to record, manage, and resolve IT problems.

Key proposal goals:

- Let users submit IT issues with contact information and device/system details.
- Organize tickets by issue category and subcategory.
- Keep the interface simple enough for users with different levels of technical experience.
- Allow tickets to be reviewed and handled by the proper support person.
- Support escalation when an issue needs higher-level support.
- Let users know when an issue is resolved.
- Collect feedback after resolution.
- Build something manageable within the given timeframe.

## 2. Final Project Result

The final project is a working Flask-based IT ticket service with a full user and admin workflow.

Implemented features:

- User login and account creation.
- Hashed password storage using Werkzeug.
- Session-based access control.
- Role-based access control for regular users and admins.
- Ticket submission form with validation.
- Issue categories and subcategories.
- User-specific My Tickets dashboard.
- Ticket detail page for viewing submitted tickets.
- Admin dashboard for viewing and managing all tickets.
- Status workflow: Open, In Progress, Escalated, Closed.
- Resolution notes for completed tickets.
- Feedback form for closed tickets.
- Filtering/search options on ticket dashboards.
- Local SQLite database storing users, tickets, and feedback.

## 3. Changes From the Original Proposal

### A. Enterprise-ready deployment became a capstone demo application

The proposal described a system that could eventually be implemented into an organization's environment. The final project is better described as a working prototype or demo. It demonstrates the core workflow, but it is not yet a fully deployed enterprise system. That is something that can be implementing in the future.

### B. Escalation was implemented as a ticket status, not automatic routing

The proposal said the system would determine whether an issue should be elevated. In the final project, escalation exists, but it is controlled by the admin/technician. The system supports escalation by allowing a ticket to be marked as Escalated and by showing that state to the user.

### C. Technician assignment was simplified into an admin dashboard

The proposal mentioned that the proper individual would work on the request. The final project has an admin/technician dashboard, but it does not assign tickets to specific technicians or departments. The organization using the service could do that manually, while that is something that can be added with more time.

### D. User resolution notification is manual/status-based, not automatic

The proposal said the user would be told when the issue was resolved. The final system shows the user the current status and resolution notes when they view their ticket, but it does not send email notifications or alerts.

### E. Solution guidance became resolution notes

The proposal said the system might give directions on how to solve the issue. The final project does not automatically generate troubleshooting steps. Instead, the admin can enter resolution notes after working the ticket.

### F. More pages were needed than originally expected

The proposal wanted the fewest pages possible. The final project uses multiple pages: login, submit ticket, My Tickets, ticket details, admin dashboard, and feedback. This is still organized, but more pages were needed to support security, user-specific views, and admin functions.

### G. Multi-user scalability was demonstrated, but not production-tested

The proposal mentioned supporting more than one person at a time and potentially scaling to many users. The final project supports multiple user accounts and separates each user's tickets, but it uses SQLite and a local Flask setup, so it should not be presented as production-scaled yet.

### H. Actual time was slightly above the original estimate

The proposal estimated about 30 hours. The documented time log shows about 34 hours. This is close to the original estimate, but the extra time came from debugging, validation, UI refinement, authentication, role-based access, and feedback logic.

## 4. Challenges Faced and Addressed

### Challenge 1: Form validation and error handling

- Added backend validation in Flask.
- Added email and phone validation.
- Displayed field-specific error messages.
- Preserved form state after validation errors.

### Challenge 2: Keeping user tickets separated

- Added login sessions.
- Stored tickets under the logged-in username.
- Filtered My Tickets and ticket details by the current session user.

### Challenge 3: Admin-only ticket management

- Added user roles.
- Added admin route protection.
- Built a separate admin dashboard for managing all tickets.

### Challenge 4: Escalation and resolution workflow

- Added ticket statuses: Open, In Progress, Escalated, Closed.
- Added status badges.
- Added resolution notes.
- Restricted feedback to closed tickets only.

### Challenge 5: Feedback timing

- Feedback page is only available when the ticket is Closed.
- Users can submit or update feedback after closure.
- Admins can view submitted feedback.

## 5. Success Points

- The project became a complete working ticket lifecycle, not just a static form.
- User authentication was added, which improved security beyond the original proposal.
- Users can only see their own tickets.
- Admins can manage all tickets from a separate dashboard.
- The Escalated status directly supports the proposal's higher-level support idea.
- Resolution notes and feedback complete the end-of-ticket workflow.
- Filtering and dashboards make the system easier to use.
- The project documentation is strong: README, scope, workflow, page plan, technology stack, testing notes, development log, and time log.

## 6. Post-Class / Future Steps

1. Deploy the app to a hosted environment instead of running it locally.
2. Replace SQLite with a production-ready database if used by many users.
3. Add email notifications when tickets are created, escalated, or closed.
4. Add technician assignment so tickets can be routed to specific support staff.
5. Add password reset and stronger account management.
6. Add audit logs for admin actions.
7. Add file attachments for screenshots or error messages.
8. Improve escalation rules with categories, priority levels, or severity levels.
9. Add a better admin creation process and remove any temporary setup scripts from a public repository.
10. Replace the development secret key with a secure environment variable before deployment.
