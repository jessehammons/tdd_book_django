from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
	@skip
	def test_cannot_add_empty_list_items(self):
		# Edith goes to the home page and accidentally tries to submit
		# an empty list item.  She hits Enter on the empty list input box
		
		# The home page refreshes, and there is an error message saying that
		# list items cannot be blank
		
		# She tries again with some text for the item, which now works
		
		# She now decides to submit a second blank list item
		
		# She receives a similar warning on the list page
		
		# And she can correct it by filling some text in
		self.fail('write me')

# no __main__, use python3 manage.py test functional_tests