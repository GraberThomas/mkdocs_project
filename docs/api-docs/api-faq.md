# FAQ - FeastVerse API

Bienvenue dans la FAQ de l'API **FeastVerse**. Cette API permet de gérer des recettes de cuisine, incluant les ingrédients, les commentaires et bien plus encore.

## 1. Général

### Est-ce que l'API est gratuite ?
Oui, l'API **FeastVerse** est entièrement gratuite d'utilisation.

### Quel est le format des réponses de l'API ?
Toutes les réponses sont retournées au format **JSON**.

### Dois-je m'authentifier pour utiliser l'API ?
Certaines fonctionnalités nécessitent une authentification via un **JWT token**, obtenu à l'aide de l'endpoint `/auth/sign-in`.

## 2. Utilisation de l'API

### Comment récupérer toutes les recettes ?

```http
GET /recipes HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer <token>
```

### Comment ajouter une nouvelle recette ?

```http
POST /recipes HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Tarte aux fraises",
  "ingredients": [
    { "name": "Fraise", "quantity": 200, "unit": "g" },
    { "name": "Sucre", "quantity": 50, "unit": "g" }
  ],
  "steps": [
    "Préparer la pâte.",
    "Découper les fraises et les disposer sur la pâte."
  ]
}
```

### Comment signaler un contenu inapproprié ?

```http
POST /reports HTTP/1.1
Host: api.feastverse.com
Authorization: Bearer <token>
Content-Type: application/json

{
  "targetId": "123e4567-e89b-12d3-a456-426614174000",
  "type": "INAPPROPRIATE_CONTENT",
  "description": "Ce commentaire est offensant."
}
```

## 3. Gestion des utilisateurs

### Comment s'inscrire ?

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

### Comment se connecter ?

```http
POST /auth/sign-in HTTP/1.1
Host: api.feastverse.com
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

Si la connexion réussit, l'API retourne un **JWT token** qui doit être inclus dans les requêtes authentifiées.

## 4. Support & Contact

### Comment obtenir de l'aide ?
Si vous avez des questions ou rencontrez des problèmes, contactez **Thomas GRABER** par email : `thomas.graber.pro@gmail.com`.

### L'API a-t-elle une documentation complète ?
Oui, la documentation complète est disponible dans l'onglet `API Docs API Endpoints - Swagger` et peut être consultée directement via l'interface utilisateur.