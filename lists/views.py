from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from lists.models import Item

# Create your views here.

HTTP_METHOD_POST = 'POST'

def home_page(request:HttpRequest):
	# if request.method == HTTP_METHOD_POST:
	# 	return HttpResponse(request.POST['item_text'])
	# return render(request, 'home.html')

	if request.method == HTTP_METHOD_POST:
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')

	items = Item.objects.all()
	return render(request, 'home.html')

def view_list(request:HttpRequest):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
