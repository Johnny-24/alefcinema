from django.shortcuts import render

menu = [
  { "id": 1, "label": "Каталог", "url": "catalog" },
  { "id": 2, "label": "Доставка", "url": "delivery" },
  { "id": 3, "label": "О компании", "url": "info" },
  { "id": 4, "label": "Контакты", "url": "contacts" }
]

cats_db = [
  { "id": 1, "name": "Лампы для проекторов", "image_name": "categoriesList1", "shield": True },
  { "id": 2, "name": "Фильтры для цифровых проекторов", "image_name": "categoriesList2", "shield": False },
  { "id": 3, "name": "Отражатели", "image_name": "categoriesList3", "shield": False },
  { "id": 4, "name": "Мебель для кинотеатров", "image_name": "categoriesList4", "shield": False },
  { "id": 5, "name": "3D оборудование", "image_name": "categoriesList5", "shield": False },
  { "id": 6, "name": "Лампы для промышленности", "image_name": "categoriesList2", "shield": False },
]

def index(request):
  return render(request, 'mainapp/index.html', { "menu": menu })

def catalog(request):
  return render(request, 'mainapp/catalog.html', { "menu": menu })

def delivery(request):
  return render(request, 'mainapp/delivery.html', { "menu": menu })

def info(request):
  return render(request, 'mainapp/info.html', { "menu": menu })

def contacts(request):
  return render(request, 'mainapp/contacts.html', { "menu": menu })
