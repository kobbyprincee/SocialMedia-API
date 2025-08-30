# Social Media API

A Django REST Framework-based social media API that allows users to create posts, follow other users, like posts, comment, and receive notifications.

## Features

- User registration and authentication (Token-based)
- Post management (CRUD operations)
- Follow/Unfollow system
- Feed of posts from followed users
- Like/Unlike posts
- Comment system
- Notification system
- Pagination and search functionality

## Technology Stack

- Django 4.2.11
- Django REST Framework 3.14.0
- SQLite (default database)
- Token Authentication

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python3 -m venv socmedapi
   source socmedapi/bin/activate  # On Windows: socmedapi\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the server:
   ```bash
   socialmedia_api/socmedapi/bin/python manage.py runserver
   ```

## API Documentation

### Authentication
All endpoints except registration and login require authentication using Token Authentication.
Include the token in the Authorization header: `Authorization: Token <your_token>`

### Endpoints

#### Authentication
- `POST /api/register/` - Register a new user
- `POST /api/login/` - Login and get token
- `GET /api/profile/` - Get current user profile

#### Posts
- `GET /api/posts/` - List all posts (paginated)
- `POST /api/posts/` - Create a new post
- `GET /api/posts/{id}/` - Get specific post
- `PUT /api/posts/{id}/` - Update post (owner only)
- `DELETE /api/posts/{id}/` - Delete post (owner only)

#### Comments
- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create a comment
- `PUT /api/comments/{id}/` - Update comment (owner only)
- `DELETE /api/comments/{id}/` - Delete comment (owner only)

#### Follow System
- `POST /api/follow/{user_id}/` - Follow a user
- `POST /api/unfollow/{user_id}/` - Unfollow a user

#### Feed
- `GET /api/feed/` - Get posts from followed users

#### Likes
- `POST /api/posts/{id}/like/` - Like a post
- `POST /api/posts/{id}/unlike/` - Unlike a post

#### Notifications
- `GET /api/notifications/` - Get user notifications
- `POST /api/notifications/{id}/read/` - Mark notification as read

### Data Models

#### Post
```json
{
  "id": 1,
  "content": "Post content",
  "media": "https://example.com/image.jpg",
  "author": "username",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### User Registration
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123",
  "bio": "User bio",
  "profile_picture": "image_file"
}
```

## Testing

### Using cURL
```bash
# Register
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'

# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'

# Create Post
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content":"My first post!"}'
```

### Using Postman
1. Set base URL: `http://localhost:8000/api`
2. Add Authorization header: `Token YOUR_TOKEN`
3. Test all endpoints with appropriate HTTP methods and JSON data
