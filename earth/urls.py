from django.urls import path
from . import views

app_name = 'earth'
urlpatterns = [
	path('wines/', views.OneWineList, name = 'wines'),
	path('', views.IndexView, name = 'index')
]