from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

HTTP_METHOD_POST = 'POST'

def home_page(request:HttpRequest):
	# if request.method == HTTP_METHOD_POST:
	# 	return HttpResponse(request.POST['item_text'])
	# return render(request, 'home.html')
	return render(request, 'home.html', {
		'new_item_text': request.POST.get('item_text', ''),
	})