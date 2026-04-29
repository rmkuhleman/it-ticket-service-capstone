# Testing Notes

## Overview
Testing was performed throughout development to ensure that all user and admin functionality worked correctly, securely, and as expected. This included debugging backend errors, validating user flows, and confirming role-based access control.


## Issues Encountered and Resolutions

### 1. Database Table Errors
**Issue:** Application failed with "no such table: users" error during login.  
**Resolution:** Added users table creation to `init_db()` to ensure it is created on startup.


### 2. Missing Logout Route
**Issue:** Application crashed due to missing `/logout` route referenced in templates.  
**Resolution:** Implemented logout route and ensured session variables were properly cleared.


### 3. Session Management Issues
**Issue:** Users were not consistently redirected or maintained in session.  
**Resolution:** Fixed session handling and ensured session variables (`username`, `role`, `last_active`) were properly set.


### 4. Role-Based Access Control Bug
**Issue:** Admin-only routes were accessible or caused errors due to incorrect decorator placement.  
**Resolution:** Implemented `admin_required` decorator correctly and applied it after `login_required`.


### 5. Flask Request Context Error
**Issue:** "Working outside of request context" error occurred due to incorrect decorator definition.  
**Resolution:** Moved decorator logic outside of route definitions and corrected structure.


### 6. Feedback Logic Issues
**Issue:** Feedback was visible or editable at incorrect times.  
**Resolution:** Restricted feedback submission to only closed tickets and ensured it updates correctly.


### 7. Resolution Notes Display
**Issue:** Resolution notes caused layout issues and appeared when not appropriate.  
**Resolution:** Limited display to closed tickets and adjusted UI styling.


### 8. Ticket Status Workflow Improvement
**Issue:** No clear way to handle unresolved tickets needing higher support.  
**Resolution:** Added "Escalated" status to ticket lifecycle and ensured it appears across all views.


## Testing Performed

- Verified user login and account creation  
- Confirmed session persistence and logout behavior  
- Tested ticket submission and validation  
- Ensured users can only view their own tickets  
- Verified admin access restrictions  
- Tested ticket status updates and bulk updates  
- Confirmed feedback submission and display logic  
- Tested escalation workflow and UI updates  


## Conclusion

Testing ensured that the application functions correctly across both user and admin workflows. Issues encountered during development were resolved through iterative debugging and validation, resulting in a stable and secure ticketing system.
