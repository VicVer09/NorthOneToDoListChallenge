from django.shortcuts import render, redirect
from items.models import Item
from django.contrib import messages
from datetime import datetime
# Create your views here.

def addItem(request):
	# return render(request, 'pages/index.html')
	if request.method == "POST":
		# SENDING A MESSAGE
		
		# Get values
		title = request.POST['title']
		if 'description' in request.POST:
			description = request.POST['description']
		else:
			description = 'No Description'

		if 'tags' in request.POST:
			tags = request.POST['tags']
		else:
			tags = 'No Tags'

		if 'due_date' in request.POST and request.POST['due_date'] != '':
			due_date = request.POST['due_date']
		else:
			due_date = datetime.now()

		message = Item.objects.create(title = title, description = description, tags = tags, due_date = due_date)
		message.save() # is this necessary?
		messages.success(request, 'Message sent!')
		
		return redirect('index')

	return render(request, 'pages/additem.html')