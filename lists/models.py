from django.db import models
from django.urls import reverse

# Create your models here.

class List(models.Model):

	def uri_list_id_uri(self):
		return reverse('view_list', args=(self.id,))


class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey(List, default=None)

#/lists/{{ list.id }}/add_item