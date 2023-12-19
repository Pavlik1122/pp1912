from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Model(models.Model):
    name = models.CharField(verbose_name='Название модели', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Cars(models.Model):
    category = models.ForeignKey(Category, verbose_name='Выберите категорию', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название категории', max_length=120)
    img = models.ImageField(verbose_name='Изображение машины', upload_to='cars/%Y/%m/%d')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    country = models.CharField(verbose_name='Страна-производитель', max_length=120)
    year = models.CharField(verbose_name='Год выпуска', max_length=55)
    model = models.ForeignKey(Model, verbose_name='Название модели', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
