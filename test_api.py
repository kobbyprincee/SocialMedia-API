#!/usr/bin/env python3
"""
Simple test script to verify API functionality
Run this after starting the Django server
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_registration():
    """Test user registration"""
    data = {
        "username": "testuser",
        "email": "test@example.com", 
        "password": "testpass123",
        "bio": "Test user bio"
    }
    response = requests.post(f"{BASE_URL}/register/", json=data)
    print(f"Registration: {response.status_code}")
    if response.status_code == 201:
        return response.json().get('token')
    return None

def test_login():
    """Test user login"""
    data = {
        "username": "testuser",
        "password": "testpass123"
    }
    response = requests.post(f"{BASE_URL}/login/", json=data)
    print(f"Login: {response.status_code}")
    if response.status_code == 200:
        return response.json().get('token')
    return None

def test_create_post(token):
    """Test post creation"""
    headers = {"Authorization": f"Token {token}"}
    data = {
        "content": "This is my first test post!",
        "media": "https://example.com/image.jpg"
    }
    response = requests.post(f"{BASE_URL}/posts/", json=data, headers=headers)
    print(f"Create Post: {response.status_code}")
    return response.json() if response.status_code == 201 else None

def test_get_posts():
    """Test getting posts"""
    response = requests.get(f"{BASE_URL}/posts/")
    print(f"Get Posts: {response.status_code}")
    return response.json() if response.status_code == 200 else None

if __name__ == "__main__":
    print("Testing Social Media API...")
    
    # Test registration
    token = test_registration()
    if not token:
        # Try login if registration fails (user might already exist)
        token = test_login()
    
    if token:
        print(f"Token obtained: {token[:20]}...")
        
        # Test post creation
        post = test_create_post(token)
        if post:
            print(f"Post created: {post['id']}")
        
        # Test getting posts
        posts = test_get_posts()
        if posts:
            print(f"Found {len(posts.get('results', []))} posts")
    else:
        print("Failed to get authentication token")