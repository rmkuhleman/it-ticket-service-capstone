# IT Ticket Service — Proposal vs. Final Project Notes

Use this as a documentation file for the presentation or as talking-point notes. The goal is not to make the project sound like it failed; the goal is to clearly explain how the approved proposal changed as the project became a working capstone application.

## 1. Proposal Background to Cover

The original proposal described an IT ticket service that would let users submit technical issues, organize those issues by category, and help determine whether the issue needed regular support, higher-level support, or a solution direction. The goal was a simple, user-friendly service that could be adapted for organizations that need a faster way to record, manage, and resolve IT problems.

Key proposal goals:

- Let users submit IT issues with contact information and device/system details.
- Organize tickets by issue category and subcategory.
- Keep the interface simple enough for users with different levels of technical experience.
- Allow tickets to be reviewed and handled by the proper support person.
- Support escalation when an issue needs higher-level support.
- Let users know when an issue is resolved.
- Collect feedback after resolution.
- Build something manageable within the capstone timeline.

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

These are the main items to document during the presentation.

### A. Enterprise-ready deployment became a capstone demo application

The proposal described a system that could eventually be implemented into an organization's environment. The final project is better described as a working prototype or capstone-ready demo. It demonstrates the core workflow, but it is not yet a fully deployed enterprise system.

How to explain it:

> The approved idea was to create a ticket service that could eventually be adapted for an organization. For the class project, I focused on building a complete working prototype that demonstrates the full ticket lifecycle instead of trying to deploy it into a real company environment.

### B. Escalation was implemented as a ticket status, not automatic routing

The proposal said the system would determine whether an issue should be elevated. In the final project, escalation exists, but it is controlled by the admin/technician. The system supports escalation by allowing a ticket to be marked as Escalated and by showing that state to the user.

How to explain it:

> The final version supports escalation, but it does not automatically decide when escalation is needed. I changed this to an admin-managed process because automatic escalation rules would require more advanced logic and more real-world support requirements than I could accurately build within the class timeline.

### C. Technician assignment was simplified into an admin dashboard

The proposal mentioned that the proper individual would work on the request. The final project has an admin/technician dashboard, but it does not yet assign tickets to specific technicians or departments.

How to explain it:

> Instead of building a full technician assignment system, I created an admin dashboard where support staff can view, update, escalate, and close tickets. Specific technician assignment would be a strong post-class improvement.

### D. User resolution notification is manual/status-based, not automatic

The proposal said the user would be told when the issue was resolved. The final system shows the user the current status and resolution notes when they view their ticket, but it does not send email notifications or alerts.

How to explain it:

> Users can track their ticket status and view resolution notes in the My Tickets area. Automatic email or alert notifications were left out of scope and would be a future improvement.

### E. Solution guidance became resolution notes

The proposal said the system might give directions on how to solve the issue. The final project does not automatically generate troubleshooting steps. Instead, the admin can enter resolution notes after working the ticket.

How to explain it:

> I kept the project realistic by having the admin provide resolution notes manually. This avoids pretending the system can automatically solve technical problems without enough information.

### F. More pages were needed than originally expected

The proposal wanted the fewest pages possible. The final project uses multiple pages: login, submit ticket, My Tickets, ticket details, admin dashboard, and feedback. This is still organized, but more pages were needed to support security, user-specific views, and admin functions.

How to explain it:

> I originally wanted the fewest pages possible, but the project needed separate pages for login, user ticket tracking, admin management, ticket details, and feedback. This made the system easier to follow and more secure.

### G. Multi-user scalability was demonstrated, but not production-tested

The proposal mentioned supporting more than one person at a time and potentially scaling to many users. The final project supports multiple user accounts and separates each user's tickets, but it uses SQLite and a local Flask setup, so it should not be presented as production-scaled yet.

How to explain it:

> The project demonstrates multi-user separation through accounts and role-based access control, but production scaling would require deployment testing, a stronger database setup, and additional security hardening.

### H. Actual time was slightly above the original estimate

The proposal estimated about 30 hours. The documented time log shows about 34 hours. This is close to the original estimate, but the extra time came from debugging, validation, UI refinement, authentication, role-based access, and feedback logic.

How to explain it:

> My original estimate was about 30 hours, and the final time log came out to about 34 hours. The extra time mainly came from improving validation, fixing session behavior, polishing the user interface, and adding role-based access control.

## 4. Challenges Faced and Addressed

Use these in the Summary of Project Results section.

### Challenge 1: Form validation and error handling

The form needed to reject incomplete or incorrect submissions while still being understandable to the user.

How it was addressed:

- Added backend validation in Flask.
- Added email and phone validation.
- Displayed field-specific error messages.
- Preserved form state after validation errors.

### Challenge 2: Keeping user tickets separated

Users should not be able to view another user's tickets.

How it was addressed:

- Added login sessions.
- Stored tickets under the logged-in username.
- Filtered My Tickets and ticket details by the current session user.

### Challenge 3: Admin-only ticket management

The project needed a difference between regular users and technicians/admins.

How it was addressed:

- Added user roles.
- Added admin route protection.
- Built a separate admin dashboard for managing all tickets.

### Challenge 4: Escalation and resolution workflow

The project needed a clear way to show progress from submission to resolution.

How it was addressed:

- Added ticket statuses: Open, In Progress, Escalated, Closed.
- Added status badges.
- Added resolution notes.
- Restricted feedback to closed tickets only.

### Challenge 5: Feedback timing

Feedback should only happen after the issue is resolved.

How it was addressed:

- Feedback page is only available when the ticket is Closed.
- Users can submit or update feedback after closure.
- Admins can view submitted feedback.

## 5. Success Points

These are the strongest results to emphasize.

- The project became a complete working ticket lifecycle, not just a static form.
- User authentication was added, which improved security beyond the original proposal.
- Users can only see their own tickets.
- Admins can manage all tickets from a separate dashboard.
- The Escalated status directly supports the proposal's higher-level support idea.
- Resolution notes and feedback complete the end-of-ticket workflow.
- Filtering and dashboards make the system easier to use.
- The project documentation is strong: README, scope, workflow, page plan, technology stack, testing notes, development log, and time log.

## 6. Post-Class / Future Steps

These directly answer the rubric item about next or additional post-class steps.

Recommended next steps:

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

## 7. Presentation Checklist Based on Rubric

### Project Background

Make sure to clearly mention:

- Original goal: create a simple IT ticket service.
- Intended users: organizations or staff needing a faster support request process.
- Problem: IT issues interrupt workflow and need organized tracking.
- Proposed solution: structured ticket submission, categorization, support review, escalation, resolution, and feedback.

### Project Results

Make sure to clearly mention:

- Final end result: working Flask ticket service.
- Challenges faced and addressed.
- Success points.
- Changes from proposal.
- Next/post-class steps.

### Demo Points

Good demo order:

1. Login page.
2. Submit a ticket.
3. Show validation briefly if needed.
4. Show My Tickets dashboard.
5. Show ticket details.
6. Switch to admin dashboard.
7. Update status to In Progress or Escalated.
8. Add resolution notes and close ticket.
9. Return as user and show resolution notes.
10. Submit feedback.

### Timing

For a 5–8 minute presentation, do not over-demo every feature. Spend most of the time on the required rubric areas:

- 1 minute: project background.
- 3–4 minutes: final project walkthrough.
- 1–2 minutes: challenges, success points, and changes from proposal.
- 1 minute: future steps.

## 8. Short Version to Say Out Loud

> My original proposal was to create a user-friendly IT ticket service that could help users submit technical problems, organize them by category, support escalation, and collect feedback after resolution. The final project accomplishes the core workflow as a Flask web application with login, ticket submission, user-specific ticket tracking, an admin dashboard, status updates, escalation, resolution notes, and feedback. Some parts changed from the original proposal. Escalation is admin-managed rather than automatic, user notifications are handled through status tracking rather than email alerts, and technician assignment was simplified into an admin dashboard. Overall, the project met the main goal of creating a functional ticket service, while the future steps would focus on deployment, notifications, technician routing, and production-level scalability.
