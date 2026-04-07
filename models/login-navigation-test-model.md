# Login and Homepage Navigation Test Model

## Scope
This model supports testing of Cambrian Moodle home page access and navigation through Microsoft SSO.

## Main states
1. User opens Moodle login page
2. User selects Microsoft sign-in
3. User completes authentication
4. User lands on Moodle home page
5. User interacts with visible homepage navigation items

## Main transitions
- Login page loads successfully
- Microsoft SSO option is visible
- Authentication succeeds
- Home page loads after authentication
- Navigation links/buttons are visible and functional

## Risks
- Login page unavailable
- Microsoft sign-in option missing
- Redirect/authentication failure
- Broken homepage links
- Homepage elements not visible after login

## Early automation focus
- Verify Moodle page is reachable
- Verify login-related content appears
- Verify homepage/navigation-related content is present
