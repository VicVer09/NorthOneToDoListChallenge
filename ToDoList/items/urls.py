from django.urls import path
from . import views


urlpatterns = [
        path('',views.index, name='items'),
        path('<int:item_id>', views.complete_idx, name = 'complete_idx'),
        path('<int:item_id>', views.complete_items, name = 'complete_items'),
        path('search', views.search, name = 'search'),
]