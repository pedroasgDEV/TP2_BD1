```markdown
# Flask API for Managing Users, Admins, and Subjects

This project is a RESTful API built using Flask, designed to manage Users, Admins, Subjects, and their relationships. It provides functionality to create, read, update, and delete records in the system as well as managing logins and connections between users/admins and subjects.

## Table of Contents

- [Installation](#installation)
- [Routes](#routes)
  - [Admins](#admins)
  - [Users](#users)
  - [Login](#login)
  - [Subjects](#subjects)
- [Testing](#testing)

## Installation

To get started, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python __main__.py
   ```

The application will be available at `http://localhost:3030`.

## Routes

### Admins

- **Create Admin:**  
  `POST /api/admins/`  
  **Body:** JSON object with admin details (e.g., name, email, password).
  
- **Get Admin:**  
  `GET /api/admins/<id>`  
  Retrieves the admin by `id`. Use `all` to get all admins.

- **Update Admin:**  
  `PUT /api/admins/<id>`  
  **Body:** JSON object with fields to update.

- **Delete Admin:**  
  `DELETE /api/admins/<id>`  
  Deletes the admin by `id`.

### Users

- **Create User:**  
  `POST /api/users/`  
  **Body:** JSON object with user details (e.g., regis_id, name, email, password).

- **Get User:**  
  `GET /api/users/<regis_id>`  
  Retrieves the user by `regis_id`.

- **Update User:**  
  `PUT /api/users/<regis_id>`  
  **Body:** JSON object with fields to update.

- **Delete User:**  
  `DELETE /api/users/<regis_id>`  
  Deletes the user by `regis_id`.

### Login

- **Login:**  
  `GET /api/login/`  
  **Body:** JSON object with email and password for login. Returns user or admin details based on the credentials.

### Subjects

- **Create Subject:**  
  `POST /api/subjects/`  
  **Body:** JSON object with subject details (e.g., subject_code, name, professor).

- **Get Subject:**  
  `GET /api/subjects/<subject_code>`  
  Retrieves the subject by `subject_code`. Use `all` to get all subjects.

- **Update Subject:**  
  `PUT /api/subjects/<subject_code>`  
  **Body:** JSON object with fields to update.

- **Delete Subject:**  
  `DELETE /api/subjects/<subject_code>`  
  Deletes the subject by `subject_code`.

- **User-Subject Connection:**  
  `POST /api/subjects/users/`  
  Creates a connection between a user and a subject.
  
  **Query Parameters:**
  - `user`: user ID
  - `subject`: subject code

- **Admin-Subject Connection:**  
  `POST /api/subjects/admins/`  
  Creates a connection between an admin and a subject.
  
  **Query Parameters:**
  - `admin`: admin ID
  - `subject`: subject code

## Testing

Testing is available to validate each module's operations. The test scripts can be found in the `/tests/` directory and executed by running the main test file:

```bash
python -m app.tests
```

You will see messages indicating whether each operation works correctly.
