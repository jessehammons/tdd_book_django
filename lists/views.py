from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm

from django.core.exceptions import ValidationError

# Create your views here.

HTTP_METHOD_POST = 'POST'

def home_page(request:HttpRequest):
	# if request.method == HTTP_METHOD_POST:
	# 	return HttpResponse(request.POST['item_text'])
	# return render(request, 'home.html')

	return render(request, 'home.html', {'form': ItemForm()})

def view_list(request:HttpRequest, list_id):
	list_ = List.objects.get(id=list_id)
	error = None
	if request.method == HTTP_METHOD_POST:
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"

	return render(request, 'lists.html', {'list':list_, 'error': error})

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
	return redirect(list_) # uses list_.get_absolute_url() under the hood

