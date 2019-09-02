from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
import string

from .models import Item
# from .models import Project
from collections import OrderedDict

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	# return render(request, 'pages/index.html')
	# reverse order (-) and parameter
	# filter removes any objects that don't fit criteria
	items = Item.objects.order_by('-due_date')
	
	paginator = Paginator(items, 9)
	page = request.GET.get('page')
	paged_items = paginator.get_page(page)
	
	context = {
		
		'items': paged_items
	
	}
	
	return render(request, 'items/items.html', context)


def complete_idx(request, item_id):
	Item.objects.filter(pk=item_id).update(is_complete=True)
	return redirect('index') 

def complete_items(request, item_id):
	Item.objects.filter(pk=item_id).update(is_complete=True)
	return redirect('items') 

def search(request):
	# return render(request, 'pages/index.html')
	queryset_list = Item.objects.order_by('-due_date') 
	
	# keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			# django special xxx__icontains parameter for case-insensitive containment test
			queryset_list = queryset_list.filter(Q(description__icontains=tags) | Q(title__icontains=tags)| Q(tags__icontains=tags)) 
	
	# tags
	if 'tags' in request.GET:
		tags = request.GET['tags']
		if tags:
			# django special xxx__icontains parameter for case-insensitive containment test
			queryset_list = queryset_list.filter(Q(tags__icontains=tags)) 
	
	# status
	if 'status' in request.GET:
		status = request.GET['status']
		if status and status != 'Type (All)':
			if status == 'Completed':
				queryset_list = queryset_list.filter(is_complete=True) 
			else:
				queryset_list = queryset_list.filter(is_complete=False) 
			
	
	paginator = Paginator(queryset_list, 9)
	page = request.GET.get('page')
	paged_items = paginator.get_page(page) 
	 
	context = {
		'items': paged_items,
		'values': request.GET
	}
	
	return render(request, 'items/search.html', context)