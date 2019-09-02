from django.shortcuts import render 
from items.models import Item

# Create your views here.
def index(request):
	# return render(request, 'pages/index.html')
	
	# get latest projects
	# change this to featured later
	items = Item.objects.order_by('-due_date').filter(is_complete=False)
	# print(projects)
	# return render(request, 'pages/index.html', {})
	# items = items[:min(5, len(items))] 
	
	context = {
	
		'items': items,

	}
	
	return render(request, 'pages/index.html', context)

def items(request):

	return render(request, 'pages/index.html')
	# return render(request, 'pages/resume.html')
