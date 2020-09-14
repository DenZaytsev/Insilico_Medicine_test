from django.db import models
from django.utils import timezone


class House(models.Model):
    """Модель дома"""
    address = models.CharField(max_length=1024, verbose_name='Адрес')
    release_date = models.DateField(verbose_name='Дата постройки', default=timezone.now)

    def __str__(self):
        return f'{self.address}'


class OrderBrick(models.Model):
    """Задание на кладку кирпичей"""
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    brick_quantity = models.PositiveIntegerField(verbose_name='количество кирпичей в заказе')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания заказа', blank=True)

    def __str__(self):
        return f'Задание от {self.created_at} для {self.house}'