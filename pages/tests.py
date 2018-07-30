from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
	def text_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def text_about_page_status_code(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code, 200)