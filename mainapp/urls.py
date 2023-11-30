from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('catalog', views.catalog, name='catalog'),
  path('delivery', views.delivery, name='delivery'),
  path('info', views.info, name='info'),
  path('contacts', views.contacts, name='contacts'),
]