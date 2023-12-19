from django.shortcuts import render, get_object_or_404

from mainapp.models import Cars


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    cars = Cars.objects.all()
    context = {
        'title': 'Автомобили',
        'cars': cars,
    }
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    context = {
        'title': 'Связаться с нами',
    }
    return render(request, 'mainapp/contact.html', context)


def select_cars(request, id):
    cars = get_object_or_404(Cars, id=id)
    context = {
        'title': {cars.name},
        'cars': cars,
    }
    return render(request, 'mainapp/select_cars.html', context)
