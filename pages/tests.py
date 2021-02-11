from django.test import SimpleTestCase
from django.urls import resolve
from django.urls import reverse

from .views import AboutPageView
from .views import HomePageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        # response = self.client.get('/pages/')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        # response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # response = self.client.get('/pages/')
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        # response = self.client.get('/pages/')
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        # response = self.client.get('/')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.',
        )

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/pages/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__,
        )

    def tearDown(self):
        super().tearDown()


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.',
        )

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/pages/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__,
        )

    def tearDown(self):
        super().tearDown()
