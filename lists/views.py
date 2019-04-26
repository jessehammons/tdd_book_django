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
	form = ItemForm()
	if request.method == HTTP_METHOD_POST:
		form = ItemForm(data=request.POST)
		if form.is_valid():
			form.save(for_list=list_)
			return redirect(list_)
	return render(request, 'lists.html', {'list':list_, 'form': form })

def new_list(request:HttpRequest):
	form = ItemForm(data=request.POST)
	if form.is_valid():
		list_ = List.objects.create()
		form.save(for_list=list_)
		return redirect(list_)  # uses list_.get_absolute_url() under the hood
	else:
		return render(request, 'home.html', {'form': form})

