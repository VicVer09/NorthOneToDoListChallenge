from django.db import models
from datetime import datetime

class Item(models.Model):
	
	### Item
	title = models.CharField(max_length = 200)
	description = models.TextField(blank = True) #: TEXT 
	tags = models.TextField(blank = True) 
	is_complete = models.BooleanField(default = False) #: BOOL [true]
	due_date = models.DateTimeField(default=datetime.now, blank = True) #: DATE
	
	def __str__(self):
		return self.title