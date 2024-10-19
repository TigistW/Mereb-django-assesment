from django.test import TestCase

# Create your tests here.
# users/tests.py
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from rest_framework import status

from Auth.models import CustomUser

class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('register')  # Adjust if your signup URL differs
        self.login_url = reverse('login')    # Adjust for your login endpoint
        self.password_reset_url = reverse('password_reset')
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "strongpassword123",
            "role":"coach"
        }
    def test_user_signup(self):
        """Test user registration with valid data."""
        response = self.client.post(self.signup_url, self.user_data)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)
    
    def test_login_with_correct_credentials(self):
        """Test login with valid credentials."""
        CustomUser.objects.create_user(**self.user_data)
        response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": "strongpassword123"
        }) 
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data) 
        
    

    def test_login_with_invalid_credentials(self):
        """Test login with incorrect credentials."""
        response = self.client.post(self.login_url, {
            "username": "wronguser",
            "password": "wrongpassword"
        })
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

