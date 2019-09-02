from django.urls import path
from . import views

urlpatterns = [
        path('addItem', views.addItem, name = 'addItem'),
]