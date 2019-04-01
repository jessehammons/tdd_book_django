from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from lists.models import Item, List

# Create your views here.

HTTP_METHOD_POST = 'POST'

def home_page(request:HttpRequest):
	# if request.method == HTTP_METHOD_POST:
	# 	return HttpResponse(request.POST['item_text'])
	# return render(request, 'home.html')

	return render(request, 'home.html')

def view_list(request:HttpRequest, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'lists.html', {'list':list_})

def new_list(request:HttpRequest):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect(f'/lists/{list_.id}/')

def add_item(request:HttpRequest, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect(f'/lists/{list_.id}/')