from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):

    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testPass123',
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            username='super_admin',
            email='superadmin@email.com',
            password='testPass123',
        )
        self.assertEqual(admin_user.username, 'super_admin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        self.username = 'newuser'
        self.email = 'newuser@email.com'

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.',
        )

    def test_signup_form(self):
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()
            [0].username, self.username,
        )
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
