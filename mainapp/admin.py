from django.contrib import admin

from mainapp.models import Category, Cars, Model

# Register your models here.
admin.site.register(Category)
admin.site.register(Cars)
admin.site.register(Model)