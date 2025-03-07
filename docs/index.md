# Welcome to FeastVerse!

Welcome to the **FeastVerse** API documentation! This API is designed to manage cooking recipes, allowing users to explore, create, and interact with recipes, comments, ingredients, and more.

## Key Features

FeastVerse provides a variety of functionalities through its endpoints:

- **Recipe Management**: Create, retrieve, and modify recipes.
- **Comments**: Add and manage comments on recipes and recipe steps.
- **Likes & Reports System**: Users can like recipes and report inappropriate content.
- **Ingredients & Ingredient Types**: Retrieve and manage the ingredients used in recipes.
- **Recipe Categories & Types**: Classify recipes by difficulty level and type.
- **User & Authentication Management**: Handle user accounts, registration, and authentication.
- **Reporting System**: Allow users to flag inappropriate or incorrect content.

## Main Endpoints

The API is structured into several sections:

### 📝 **Comments**
Manage comments related to recipes and recipe steps.

### 🍽️ **Recipes**
Access recipes, interact with them (likes, reports, comments), and explore their steps.

### 📊 **Categories & Types**
Retrieve different difficulty categories, recipe types, and ingredient measurement units.

### 👤 **Users & Authentication**
User registration, authentication, and profile management.

### ⚠️ **Reports**
Flag inappropriate or incorrect content on the platform.

### 🥕 **Ingredients**
Manage and classify ingredients used in recipes.

## Format & Authentication

- **Response Format**: All data is exchanged in JSON.
- **Authentication**: Access to certain features requires a JWT token obtained via `/auth/sign-in`.

## Example Request

A request to retrieve all recipes:

```http
GET /recipes HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer <token>
```