from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
import lists.views

from lists.models import Item, List

import bs4

class ListViewTest(TestCase):

#	from django.urls import resolve

	def test_resolves_to_list_view(self):
		view, args, kwargs = resolve('/lists/321/')
		self.assertEqual(view, lists.views.view_list)
		self.assertEqual(321, int(args[0]))

	def test_uses_list_template(self):
		list = List.objects.create()
		response = self.client.get(f'/lists/{list.id}/')
		self.assertTemplateUsed(response, 'lists.html')

	def test_displays_only_items_for_that_list(self):
		correct_list = List.objects.create()
		Item.objects.create(text='item one', list=correct_list)
		Item.objects.create(text='item two', list=correct_list)
		other_list = List.objects.create()
		Item.objects.create(text='other list item one', list=other_list)
		Item.objects.create(text='other list item two', list=other_list)

		response = self.client.get(f'/lists/{correct_list.id}/')

		self.assertContains(response, 'item one')
		self.assertContains(response, 'item two')
		self.assertNotContains(response, 'other list item one')
		self.assertNotContains(response, 'other list item two')

	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get(f'/lists/{correct_list.id}/')
		self.assertEqual(response.context['list'], correct_list)


class HomePageTest(TestCase):

	def test_home_html(self):
		response = self.client.get('/')
		self.assertTrue(response.status_code, 200)
		self.assertTrue(response['Content-Type'], 'text/html')
		soup = bs4.BeautifulSoup(response.content, 'lxml')
		html_tags = soup.findAll('html')
		self.assertEqual(len(html_tags), 1, msg='expected one and only one <html> tag')
		title_tags = html_tags[0].findAll('title')
		self.assertEqual(len(title_tags), 1, msg='expected one and only one <title> tag')
		title_tag = title_tags[0]
		self.assertEqual(str(title_tag.string), 'To-Do lists')
		body_tags = html_tags[0].findAll('body')
		self.assertEqual(len(body_tags), 1, msg='expected one and only one <body> tag')
		h1_tags = body_tags[0].findAll('h1')
		self.assertEqual(len(h1_tags), 1, msg='expected one and only one <h1> tag')
		h1_tag = h1_tags[0]
		self.assertEqual(str(h1_tag.string), 'Start a new To-Do list')
		form_tags = body_tags[0].findAll('form')
		self.assertEqual(len(form_tags), 1, msg='expected one and only one <form> tag')
		form_tag = form_tags[0]
		form_tag_attrs = form_tag.attrs
		self.assertEqual(form_tag_attrs['method'], 'POST', msg='expected form method POST')
		expected_action_uri = '/lists/new'
		self.assertEqual(form_tag_attrs['action'], expected_action_uri, msg='expected correct action uri')

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')



class NewListTest(TestCase):
	def test_can_save_a_POST_request(self):
		item_text_value = 'A new list item'
		response = self.client.post('/lists/new', data={'item_text':item_text_value})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, item_text_value)

	def test_redirects_after_POST(self):
		response = self.client.post('/lists/new', data={'item_text':'A new list item'})
		new_list = List.objects.first()
		self.assertRedirects(response, f'/lists/{new_list.id}/')

class NewItemTest(TestCase):

	def test_resolves_to_add_item_view(self):
		view, args, kwargs = resolve('/lists/3/add_item')
		self.assertEqual(view, lists.views.add_item)

	def test_can_save_a_POST_request_to_an_existing_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text':'A new item for an existing list'})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new item for an existing list')
		self.assertEqual(new_item.list, correct_list)

	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		response = self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item for an existing list'})

		self.assertRedirects(response, f'/lists/{correct_list.id}/')


class ListAndItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first ever list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first ever list item')
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(first_saved_item.list, list_)
