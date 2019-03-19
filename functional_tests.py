from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online todo app.  She goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention todo lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('finish the test later')

		# She is invited to enter a todo item straight away

		# She types "Buy Peacock feathers" into a text box

		# When she hits enter, the page updates, and now the page lists "Buy peacock feathers" as an item in a todo list

		# There is still a text box inviting her to add another item.  She enters "Use Peacock feathers to make a fly"

		# The page updates again, and now shows both items on her list

		# Edith wonders whether the site will remember her list.
		# Then she sees that the site has generated a unique URL for her,
		# there is some explanitory text to that effect

		# She visits that URL, her todo list is still there

		# Satisfied, Edith goes back to sleep

if __name__ == '__main__':
	unittest.main()