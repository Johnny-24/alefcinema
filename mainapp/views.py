from django.shortcuts import render

menu = [
  { "id": 1, "label": "Каталог", "url": "catalog" },
  { "id": 2, "label": "Доставка", "url": "delivery" },
  { "id": 3, "label": "О компании", "url": "about" },
  { "id": 4, "label": "Контакты", "url": "contacts" }
]

def index(request):
  return render(request, 'mainapp/index.html', { "menu": menu })

def catalog(request):
  return render(request, 'mainapp/catalog.html', { "menu": menu })

def delivery(request):
  return render(request, 'mainapp/delivery.html', { "menu": menu })

def about(request):
  return render(request, 'mainapp/about.html', { "menu": menu })

def contacts(request):
  return render(request, 'mainapp/contacts.html', { "menu": menu })
