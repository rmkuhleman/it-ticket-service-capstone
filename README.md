# IT Ticket Service Capstone

This capstone project focuses on creating an IT ticket service that allows users to submit technical issues, enables technicians to review and update tickets, and supports escalation, resolution, and feedback.

## Current Status
The project now includes secure user authentication with hashed passwords and session-based access control, ensuring users can only view their own tickets. Ticket submission, confirmation, and user-specific views are fully functional, and the My Tickets page has been streamlined into a clean summary dashboard with description previews and resolution note indicators. The admin view supports full ticket management, including status and resolution note updates (individual and bulk). The system is stable, consistent in UI, and ready for final enhancements such as feedback features and minor refinements.

## Documentation

Detailed project documentation can be found in the `/docs` folder, including:
- Development logs
- Testing notes
- Workflow diagrams
- Time tracking
- [Project Scope](docs/project-scope.md)
- [Workflow Diagram](docs/workflow-diagram.md)

## Current Capstone Progress

### User Experience
![My Tickets Dashboard](images/updated-login-page.png)
*Secure login page with username and password authentication, supporting both new account creation and returning user access.*

![My Tickets Dashboard](images/updated-my-ticket-page.png)
*User-specific ticket dashboard displaying submitted tickets with filtering options and real-time status tracking.*

### Ticket Management
![My Tickets Dashboard](images/updated-progress-ticket-details-page.png)
*Detailed view of a submitted ticket showing all relevant information while the issue is still in progress.*

![My Tickets Dashboard](images/updated-closed-ticket-details-page.png)
*Completed ticket view displaying final resolution notes once the issue has been marked as closed.*

### Admin Interface
![My Tickets Dashboard](images/updated-admin-page.png)
*Administrative dashboard for managing all tickets, including status updates, resolution notes, and bulk update functionality.*
