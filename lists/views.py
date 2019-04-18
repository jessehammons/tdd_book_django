from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from lists.models import Item, List

from django.core.exceptions import ValidationError

# Create your views here.

HTTP_METHOD_POST = 'POST'

def home_page(request:HttpRequest):
	# if request.method == HTTP_METHOD_POST:
	# 	return HttpResponse(request.POST['item_text'])
	# return render(request, 'home.html')

	return render(request, 'home.html', {'uri_action_new_list':List.URI_ACTION_NEW_LIST})

def view_list(request:HttpRequest, list_id):
	list_ = List.objects.get(id=list_id)
	if request.method == HTTP_METHOD_POST:
		Item.objects.create(text=request.POST['item_text'], list=list_)
		return redirect(list_.uri_list_id_uri())
	return render(request, 'lists.html', {'list':list_, 'list_uri_action_add_item':list_.uri_action_add_item()})

def new_list(request:HttpRequest):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect(list_.uri_list_id_uri())

