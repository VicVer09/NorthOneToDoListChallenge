from django.contrib import admin 
from .models import Item

# https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#modeladmin-objects
class ItemAdmin(admin.ModelAdmin):
	
	list_display = ('title', 'is_complete', 'due_date', 'tags')
	list_display_links = ('title', 'due_date', 'tags')
	list_filter = (['is_complete'])
	list_editable = (['is_complete'])
	search_fields = ('title', 'description','is_complete', 'due_date', 'tags')
	list_per_page = 50

# Register your models here.
admin.site.register(Item, ItemAdmin)