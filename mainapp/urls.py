from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('contact/', mainapp.contact, name='contact'),
    path('catalog/cars/<int:id>/', mainapp.select_cars, name='select_cars'),
]
