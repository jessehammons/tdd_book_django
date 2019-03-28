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
		return redirect('/')

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})