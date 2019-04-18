from django.db import models

# Create your models here.

class List(models.Model):
	URI_ACTION_NEW_LIST = '/lists/new'
	URI_BASE = '/lists'

	def uri_action_add_item(self):
		return f'{self.URI_BASE}/{self.id}/'

	def uri_list_id_uri(self):
		return f'{self.URI_BASE}/{self.id}/'


class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey(List, default=None)

#/lists/{{ list.id }}/add_item