from django.db import models
from seller.models import Seller


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name='products',
                               verbose_name='Продавец')
    categories = models.ManyToManyField(Category, related_name='products',
                                        verbose_name='Категории')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
