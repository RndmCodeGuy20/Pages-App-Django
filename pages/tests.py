from django.test import SimpleTestCase, TestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def tes_about_page_status(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
