from django.test import SimpleTestCase


# Create your tests here.

class HomePageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
