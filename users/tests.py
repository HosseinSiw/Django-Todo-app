from django.test import TestCase, Client
from django.urls import reverse
from .models import User
from .forms import LoginForm, SignUpForm


class CustomLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('users:login')
        User.objects.create_user(username='testuser', password='testpass', email='email@email.com')

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login_page.html')

    def test_login_view_post_success(self):
        response = self.client.post(self.login_url, {
            "email": "email@email.com",
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertTrue(response.url.startswith(''))  # Assuming 'home:home' resolves to '/home/home/'

    def test_login_view_post_failure(self):
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpass',
            "email": "wrongemail@wrongemail.com",
        })
        self.assertEqual(response.status_code, 302)  # Redirects even on failure
        self.assertTrue(response.url.endswith(reverse('users:login')))  # Should redirect back to login


class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('users:signup')

    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup_page.html')

    def test_signup_view_post_success(self):
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertTrue(User.objects.filter(username='newuser').exists())  # User should be created
        self.assertTrue(response.url.endswith(reverse('users:login')))  # Redirect to login page

    def test_signup_view_post_failure(self):
        response = self.client.post(self.signup_url, {
            'email': 'admin@admin.com',  # Assuming this user already exists
            'username': 'hossein',
            'password1': '123',
            'password2': '123'
        })
        self.assertEqual(response.status_code, 200)  # Form errors, so not redirected
        self.assertTemplateUsed(response, 'users/signup_page.html')
