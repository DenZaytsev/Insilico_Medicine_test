from django.db import models
from django.utils import timezone


class House(models.Model):
    """Модель дома"""
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    release_date = models.DateField(verbose_name='Дата постройки', default=timezone.now)


class OrderBrick(models.Model):
    """Задание на кладку кирпичей"""
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    brick_quantity = models.PositiveIntegerField(verbose_name='количество кирпичей в заказе')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')