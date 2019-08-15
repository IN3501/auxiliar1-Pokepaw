from django.contrib import admin
from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
	path('', views.index, name='index'),
	path('pestaña/', views.pestaña, name='pestaña'),
	path('pestaña2/', views.pestaña2, name='pestaña2'),
]
