from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


class TestAPI(TestCase):

    def setUp(self):
        user_obj = get_user_model().objects.create(email='testuser@gmail.com')
        self.client = APIClient()
        self.client.force_authenticate(user=user_obj)

    def test_method(self):
        self.assertEqual('Test Demo', 'Test Demo')
