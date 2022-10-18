from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(
        to='market.Product',
        verbose_name='Тип',
        related_name='orders',
        blank=True
    )
    user_name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=200,
        null=False,
        blank=False
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=200,
        null=False,
        blank=False
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=200,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.user_name} {self.phone} {self.address}'
