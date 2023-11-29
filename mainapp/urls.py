from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('catalog', views.catalog, name='catalog'),
  path('delivery', views.delivery, name='delivery'),
  path('about', views.about, name='about'),
  path('contacts', views.contacts, name='contacts'),
]