from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class ApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_health_check(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'healthy')

    def test_status_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('cpu_usage', response.data)

    def test_status_unauthenticated(self):
        url = reverse('status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
