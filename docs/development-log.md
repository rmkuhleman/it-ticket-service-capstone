# Development Log

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
