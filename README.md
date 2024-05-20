# QA Automation Technical task for Очень Интересно

## Overview

This project is a QA automation package developed for a technical task. The package includes test cases for the website, focusing on the login and post functionality. The project uses Selenium WebDriver for browser automation and Pytest to run tests.

## Tests

### 1. Successful Log in

- **Description**: Test verifies that a user can successfully log in to the website.
- **Steps**:
  - Open page for admin login (link saved in GitHub secrets)
  - Log in using correct existing user credentials (credentials saved in GitHub secrets)
- **Result**: User is logged in, dashboard page is opened

### 2. Successful post creation

- **Description**: This test verifies that a user can successfully create a post with valid data.
- **Pre-condition**: user is logged in.
- **Steps**:
  -  Open the create post form (link saved in GitHub secrets)
  -  Fill all fields correctly (field rules are specified in the specification)
  -  Click _**Create!**_ button
- **Result**:
  - **Following notification is shown**: Post was successfully created!
  - **Created post is shown on Dashboard page with filled**: author, title, creation date fields.

### 3. Validation messages about required fields are shown after focus change

- **Description**: This test verifies that appropriate validation messages are displayed when the user tries to submit the post creation form with empty fields.
- **Pre-condition**: user is logged in.
- **Steps**:
  -  Open the create post form (link saved in GitHub secrets)
  -  Click _**Create!**_ button
- **Result**:  validation messages are shown under required fields.

## Linters and CI/CD

### Pre-commit hooks

Linters are configured to run as pre-commit hooks to ensure code quality. The hooks will automatically check the code before any commit.

### GitHub Actions

Linters are executed automatically upon pushing to the main branch using GitHub Actions.

Running tests is also implemented in GitHub actions using workflow_dispatch.
