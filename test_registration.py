#!/usr/bin/env python3
import requests
import json

# Test registration with POST method
url = "http://localhost:8000/api/register/"
data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "bio": "Test user"
}

response = requests.post(url, json=data)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")