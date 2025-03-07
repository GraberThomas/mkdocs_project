# FeastVerse API Authentication Guide

FeastVerse provides a secure authentication system that assigns roles to users, ensuring proper access control to API endpoints. This guide explains how users can authenticate and what permissions are granted based on their role.

## User Registration and Authentication

### 1. User Registration
Users can register an account using the `/auth/signup` endpoint. This requires providing details such as username, email, and password.

**Endpoint:**
- `POST /auth/signup`: Registers a new user.

**Example Request:**
```http
POST /auth/signup HTTP/1.1
Host: api.feastverse.com
Content-Type: application/json

{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "securepassword"
}
```

### 2. User Authentication
After registration, users can log in using the `/auth/sign-in` endpoint. Upon successful authentication, the API returns a JWT token.

**Endpoint:**
- `POST /auth/sign-in`: Authenticates a user and returns a JWT token.

**Example Request:**
```http
POST /auth/sign-in HTTP/1.1
Host: api.feastverse.com
Content-Type: application/json

{
  "username": "newuser",
  "password": "securepassword"
}
```

**Example Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## Using the JWT Token
The JWT token must be included in the `Authorization` header for requests to protected endpoints. The token should be prefixed with `Bearer`.

**Example Request with JWT Token:**
```http
GET /recipes HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Role-Based Access Control
Users in FeastVerse have different roles, which determine their access permissions:

- **STANDARD**: Regular users with basic access.
- **MODERATOR**: Users with elevated permissions to manage content.
- **ADMINISTRATOR**: Full access to all resources and administrative actions.

Certain endpoints return different data or restrict access based on the user's role.

## Endpoint Authentication Requirements

### Public Endpoints (No Authentication Required)
- `GET /comments/{commentId}`: Retrieve comment details.
- `GET /comments`: Retrieve all comments.
- `GET /recipes/difficulties`: Retrieve difficulty categories.
- `GET /recipes/types/{typeId}`: Retrieve a recipe type by ID.
- `GET /recipes/types`: Retrieve all recipe types.
- `GET /recipes/{recipeId}`: Retrieve a recipe by ID.
- `GET /recipes`: Retrieve all recipes.
- `GET /ingredients`: Retrieve all ingredients.
- `GET /ingredients/{ingredientId}`: Retrieve ingredient details.
- `GET /ingredients/types`: Retrieve all ingredient types.
- `GET /ingredients/types/{typeId}`: Retrieve ingredient type by ID.

### Protected Endpoints (Authentication Required)
- `PUT /comments/{commentId}`: Update a comment.
- `DELETE /comments/{commentId}`: Delete a comment.
- `PUT /recipes/types/{typeId}`: Update a recipe type.
- `DELETE /recipes/types/{typeId}`: Delete a recipe type.
- `POST /recipes/types`: Create a recipe type.
- `POST /recipes/{recipeId}/reports`: Create a report for a recipe.
- `POST /recipes/{recipeId}/like`: Like a recipe.
- `DELETE /recipes/{recipeId}/like`: Remove a like.
- `POST /recipes/{recipeId}/comments`: Post a comment on a recipe.
- `POST /recipes/steps/{stepId}/reports`: Report an issue with a recipe step.
- `POST /recipes/steps/{recipeStepId}/comments`: Post a comment on a recipe step.
- `POST /reports`: Create a report.
- `DELETE /reports/{reportId}`: Delete a report.
- `PATCH /reports/{reportId}`: Update a report.
- `GET /users/{userId}`: Retrieve user details.
- `DELETE /users/{userId}`: Delete a user.

By following these authentication and authorization guidelines, users can securely interact with the FeastVerse API based on their role and permissions.