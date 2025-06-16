from django.shortcuts import render, HttpResponse
from .models import Car

def cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/cars.html.jinja', context)

def car(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {'car': car}
    return render(request, 'cars/car.html.jinja', context)

def category(request, category_name):
    cars = Car.objects.all().filter(category=category_name)
    category = Car.get_car_category(category_name)
    context = {'cars': cars, 'category': category}
    return render(request, 'cars/category.html.jinja', context)

def categories(request):
    categories = Car.get_all_categories()
    context = {'categories': categories}
    return render(request, 'cars/categories.html.jinja', context)