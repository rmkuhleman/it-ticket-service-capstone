# Development Log

Development of this project began with planning and proposal approval in early March, followed by focused implementation and refinement during early-mid April.

## Work Session 1 - Repository Setup and Planning
Date: April 14, 2026

### What I worked on
- Created the GitHub repository
- Created the documentation files
- Completed and refined the project scope document
- Created the workflow document
- Updated the README file

### Outcome
- The basic repository and documentation structure for the project are now in place.
- The project scope and workflow are now clearly documented.
- The README now provides a better summary of the project and its documentation.

### Next Step
- Create the page plan and screen layout for the system.

## Work Session 2 - Page Planning and Technology Planning
Date: April 15, 2026

### What I worked on
- Created the page plan document
- Defined the main screens of the IT Ticket Service
- Organized the purpose and elements of each page
- Created the technology stack document
- Chose the main tools and frameworks for the project
- Defined the planned project structure

### Outcome
- The main pages of the system are now planned out and documented.
- The screen structure now supports the workflow and scope of the project.
- The main development tools for the project are now documented.
- The planned file and folder structure for the application is now in place.

### Next Step
- Set up the actual project files and create the first Flask app page.

## Work Session 3 - Project Setup and Initial Form Development
Date: April 20, 2026

### What I worked on
- Opened the project locally in VS Code
- Set up the local Python environment
- Installed Flask
- Created the base project files and folders
- Created the initial Flask app and page structure
- Connected the CSS file to the page
- Built the static ticket submission form layout
- Added category-based subcategory dropdown behavior using JavaScript
- Removed the temporary alert used for testing

### Outcome
- The project has moved from planning into implementation.
- The local Flask environment is working correctly.
- The main ticket submission page now loads successfully in the browser.
- The form layout is now visible and styled.
- The issue category dropdown now updates the subcategory dropdown with relevant options.

### Next Step
- Make the form submit to Flask and begin handling the entered ticket data.

## Work Session 4 - Form Validation, Error Handling, and UX Refinement
Date: April 23, 2026

### What I worked on
- Refactored Flask backend validation to enforce all required rules server-side
- Removed browser-based validation using `novalidate` for consistent behavior
- Standardized field naming across Flask, HTML, and JavaScript for consistent mapping
- Implemented structured error handling using field-based error objects
- Updated frontend to display validation errors using a centralized error list
- Added email format validation using regex-based checking
- Added phone number validation with flexible formatting support
- Improved error messaging for clarity and usability
- Implemented per-field error dismissal in JavaScript
- Fixed issue where unrelated validation errors disappeared when editing a single field
- Resolved sessionStorage persistence issue for category/subcategory selection
- Adjusted form state reset behavior when submitting or restarting a new ticket
- Improved overall form UX consistency and validation flow

### Outcome
- The form now uses a fully centralized Flask validation system
- Error messages are structured and correctly mapped to individual fields
- Users receive clearer and more accurate validation feedback
- Frontend behavior is now consistent and predictable across all fields
- Form persistence and reset behavior now works correctly without leftover state issues
- The system is significantly more stable and closer to production-quality form handling

### Next Step
- Improve UI feedback further by visually highlighting invalid fields (e.g., red borders)
- Optional enhancement: add real-time validation while typing for better user experience

## Work Session 5 – Ticket List Page Enhancements and Bulk Update Logic
**Date:** April 24, 2026

### What I worked on
- Ensured category → subcategory selection persists through invalid form submissions using `sessionStorage`.
- Added “dirty state” tracking (`data-dirty`) to ticket status dropdowns to prevent bulk updates from overwriting unchanged tickets.
- Updated `tickets.html` layout: added `.reset-btn` class for Reset button, aligned filters using `.ticket-filter-form`.
- Refactored JavaScript for bulk update to only send tickets marked as modified.
- Minor CSS adjustments for consistent spacing and visual alignment of ticket cards and filter controls.
- Fixed Reset button alignment to match Apply button perfectly.
- Adjusted filter input fields and dropdowns to prevent text clipping in ticket status options.
- Updated JavaScript so the "Update All" button properly updates colored status badges on tickets without interfering with individual updates.
- Prevented page from scrolling to top when individual ticket status is updated.
- Verified that individual ticket updates and bulk updates operate independently and correctly.
- Additional CSS refinements for dropdown visibility, spacing, and overall visual consistency.

### Outcome
- Subcategory selection now persists correctly across page reloads and invalid submissions.
- Bulk Update button updates only tickets with changed status.
- Reset button fully aligned and visually consistent with Apply button.
- Status dropdowns display full text without clipping.
- Status badges now update dynamically during bulk updates without affecting individual ticket functionality.
- Page no longer jumps to the top when updating tickets.
- Frontend logic is more robust, polished, and reliable for single and bulk ticket operations.

### Next Step
- Implement backend logic to filter tickets based on search, status, and sort selections.
- Build user-facing ticket status page to allow users to view only their submitted tickets.
- Begin work on submission confirmation page enhancements and feedback page setup.

## Work Session 6 – Ticket Submission Page Refinements and My Tickets Integration
**Date:** April 25, 2026

### What I worked on
- Connected the “View Details” button from the My Tickets page to the ticket submission confirmation page (`confirm.html`), enabling users to view a specific ticket’s details.
- Added a “Back to My Tickets” button on the Ticket Submitted page for easier navigation without relying on the browser back button.
- Added the ticket status display to the Ticket Submitted page for consistency with My Tickets page.
- Matched the visual style of the status badge on the Ticket Submitted page to match the My Tickets page (oval shape, gray background, colored text).
- Standardized description box styling across pages: scrollable box on the Ticket Submitted page and a shorter preview box on the My Tickets page.
- Implemented text truncation for the description preview on My Tickets page with ellipsis to indicate overflow.
- Fixed description preview box overflow issues, ensuring text was not cut off mid-line and maintained consistent layout.
- Adjusted CSS for scrollable description boxes to prevent horizontal scrolling and improve readability.
- Ensured all updates preserved existing form validation, session handling, and My Tickets page functionality.
- Verified all navigation links, status badges, and description displays remained consistent and visually aligned across pages.

### Outcome
- Users can now navigate directly from Ticket Submitted page to their list of submitted tickets.
- Status information is displayed consistently across pages, improving clarity for users.
- Description previews on My Tickets page are visually clean and truncated properly with ellipsis, without cutting off text mid-line.
- Ticket Submitted page now displays the full ticket description in a scrollable box, matching form page style.
- All changes preserved current form validation, submission, and error handling behavior.

### Next Step
- Review and optimize CSS styling further for mobile responsiveness.
- Implement additional ticket detail enhancements (e.g., resolution notes, assigned technician view).
- Optionally add real-time status update notifications to My Tickets page.

## Work Session 7 – User-Specific Ticket Isolation and Session Management
**Date:** April 26, 2026

### What I worked on
- Debugged `/my_tickets` page to ensure tickets displayed only for the logged-in user.
- Updated ticket submission logic to pull username from session instead of the form input, eliminating potential cross-user ticket display.  
- Fixed login flow so that users remain logged in for the duration of their browser session.  
- Added logout functionality with a “Switch User” button on the My Tickets page for immediate session clearing.  
- Implemented inactivity-based logout across all tabs, automatically signing out users after 15 minutes of no activity (mouse, keyboard, scroll, touch).  
- Ensured activity in any tab resets the inactivity timer for all open tabs.  
- Added explanatory text on the login page guiding new and returning users on how to use the username field.  
- Verified that session persists properly until browser closes or inactivity logout triggers; no “remember me” option implemented for security.  
- Confirmed that filtering on My Tickets page (ticket ID, category, subcategory, description, date) continues to function correctly for user-specific tickets.  
- Ensured ticket detail pages (`confirm.html`) only show information for the logged-in user.  
- Preserved all existing features, including form validation, status badges, description box styling, and navigation links.  
- Tested logout behavior to ensure session clears and no residual ticket information is accessible in any tab.  

### Outcome
- Users now see only their own tickets on the My Tickets page.  
- Session-based login and inactivity logout ensure security and user-specific ticket isolation.  
- Ticket filters and detail views function correctly without affecting other users.  
- Login guidance improves user understanding for new and returning users.  
- System is stable, and all previously working features remain intact.  

### Next Step
- Monitor session behavior across different browsers for consistency.  
- Begin cosmetic or UX refinements if desired (e.g., mobile responsiveness, styling tweaks).  
- Plan enhancements for ticket detail page (resolution notes, technician assignments) in upcoming sessions.

## Work Session 8 – Authentication, Security Enhancements, and UI Refinement
**Date:** April 27, 2026

### What I worked on
- Implemented a full authentication system using usernames and passwords.
- Created a new `users` table in the database to securely store account credentials.
- Added password hashing using Werkzeug (`generate_password_hash`, `check_password_hash`) to prevent storing plaintext passwords.
- Updated login flow to support both account creation (new users) and authentication (existing users).
- Enforced session-based authentication across the application using `login_required`.
- Restored and integrated logout functionality, allowing users to securely end sessions.
- Fixed database initialization issues related to missing tables (`users`) and ensured proper creation on startup.
- Replaced deprecated `datetime.utcnow()` usage with `datetime.now()` for improved compatibility.
- Verified secure access control so users can only view their own tickets and details.
- Refactored My Tickets page into a cleaner summary/dashboard view:
  - Removed sensitive or redundant fields (email, phone, machine ID, full resolution notes).
  - Added description preview with line clamping and ellipsis for better readability.
  - Added a visual alert when resolution notes are available without exposing full content.
- Improved UI/UX consistency between admin and user ticket views.
- Enhanced resolution notes display styling and ensured persistence after updates and page refreshes.
- Updated bulk update functionality to support both ticket status and resolution notes simultaneously.
- Improved bulk update feedback messaging and UI positioning.
- Refined layout and spacing across ticket cards, filters, and action buttons for better usability.
- Ensured all filtering features (ID, category, subcategory, description, date) continue functioning correctly.
- Conducted full regression testing to confirm no previously working features were broken.

### Outcome
- Secure authentication system successfully implemented with hashed passwords.
- Users can now safely create accounts and log in without risk of unauthorized ticket access.
- Application enforces proper session handling and route protection.
- My Tickets page is now a clean, user-friendly summary dashboard.
- Admin functionality remains intact with improved bulk update capabilities.
- UI is more consistent, readable, and aligned with real-world helpdesk systems.
- System remains stable with all existing functionality preserved.

### Next Step
- Consider adding a feedback system for users after tickets are marked as closed.
- Optionally implement role-based access (admin vs user accounts).
- Perform final UI polish and prepare for presentation/demo.
- Practice explaining system architecture, authentication flow, and security decisions.

## Work Session 9 – Feedback System, Escalation Workflow, and Finalization
**Date:** April 28, 2026

### What I worked on
- Implemented a full feedback system allowing users to submit ratings and comments for closed tickets.
- Created a `feedback` table in the database and integrated it with both user and admin views.
- Ensured feedback can only be submitted for closed tickets and can be updated if needed.
- Integrated feedback display into the admin dashboard for technician review.
- Added role-based access control by introducing a `role` field in the users table.
- Implemented `admin_required` decorator to restrict access to admin-only routes.
- Configured login flow to redirect admins to the `/tickets` dashboard and users to `/my_tickets`.
- Removed temporary admin privilege route (`/make_admin`) after assigning admin role directly in the database.
- Added "Escalated" as a new ticket status and integrated it into the full ticket lifecycle.
- Updated admin dashboard to allow selection of Escalated status and ensured it displays correctly across all views.
- Added visual indicator and styling for escalated tickets to improve clarity in the UI.
- Refined status badge colors to clearly distinguish Open, In Progress, Escalated, and Closed states.
- Performed full system testing to confirm:
  - User and admin workflows function correctly
  - Role-based access is enforced
  - Feedback logic works as intended
  - Escalation status updates properly across all pages
- Finalized project documentation:
  - Updated README to reflect completed features
  - Revised project scope, page plan, and workflow documents to match implementation
  - Completed testing notes to document issues encountered and resolved
  - Organized all documentation into the `/docs` folder

### Outcome
- The system now includes a complete ticket lifecycle with escalation and feedback.
- Role-based access control ensures proper separation between user and admin functionality.
- Admins can manage tickets, view feedback, and escalate issues as needed.
- Users can track tickets, view resolution details, and provide feedback after completion.
- All documentation is now accurate, complete, and aligned with the implemented system.
- The project is stable, fully functional, and ready for submission.

### Next Step
- Final review of submission materials
- Capture final screenshots for documentation
- Submit project to Canvas
