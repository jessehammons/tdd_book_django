from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

	# def test_root_url_resolves_to_home_page(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, home_page)
	# 
	# def test_home_page_returns_correct_html(self):
	# 	# request = HttpRequest()
	# 	# response = home_page(request)
	# 	response = self.client.get('/')
	# 	html = response.content.decode('utf8')
	# 	self.assertTrue(html.startswith('<html>'))
	# 	self.assertIn('<title>To-Do lists</title>', html)
	# 	self.assertTrue(html.strip().endswith('</html>'))
	# 
	# 	self.assertTemplateUsed(response, 'home.html')

	def test_only_saves_items_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		item_text_value = 'A new list item'
		response = self.client.post('/', data={'item_text':item_text_value})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, item_text_value)

	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'item_text':'A new list item'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_display_all_list_items(self):
		Item.objects.create(text='item_one')
		Item.objects.create(text='item_two')

		response = self.client.get('/')

		self.assertIn('item_one', response.content.decode())
		self.assertIn('item_two', response.content.decode())


from lists.models import Item

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first ever list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first ever list item')
		self.assertEqual(second_saved_item.text, 'Item the second')
