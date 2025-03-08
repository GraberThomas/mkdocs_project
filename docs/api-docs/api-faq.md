# FAQ - FeastVerse API

Welcome to the **FeastVerse** API FAQ. This API allows you to manage cooking recipes, including ingredients, comments, and much more.

## 1. General

### Is the API free?
Yes, the **FeastVerse** API is completely free to use.

### What is the response format of the API?
All responses are returned in **JSON** format.

### Do I need to authenticate to use the API?
Some features require authentication via a **JWT token**, obtained using the `/auth/sign-in` endpoint.

## 2. Using the API

### How to retrieve all recipes?

```http
GET /recipes HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer <token>
```

### How to add a new recipe?

```http
POST /recipes HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Strawberry Tart",
  "ingredients": [
    { "name": "Strawberry", "quantity": 200, "unit": "g" },
    { "name": "Sugar", "quantity": 50, "unit": "g" }
  ],
  "steps": [
    "Prepare the dough.",
    "Cut the strawberries and place them on the dough."
  ]
}
```

### How to report inappropriate content?

```http
POST /reports HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer <token>
Content-Type: application/json

{
  "targetId": "123e4567-e89b-12d3-a456-426614174000",
  "type": "INAPPROPRIATE_CONTENT",
  "description": "This comment is offensive."
}
```

## 3. User Management

### How to sign up?

```http
POST /auth/signup HTTP/1.1
Host: api.feastverse.com
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securePassword123",
  "pseudo": "GourmetUser"
}
```

### How to log in?

```http
POST /auth/sign-in HTTP/1.1
Host: api.feastverse.com
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

If the login is successful, the API returns a **JWT token** that must be included in authenticated requests.

## 4. Support & Contact

### How to get help?
If you have questions or encounter issues, contact **Thomas GRABER** via email: `thomas.graber.pro@gmail.com`.

### Does the API have complete documentation?
Yes, the full documentation is available in the `API Docs / API FAQ` file and can be accessed directly via the user interface.
