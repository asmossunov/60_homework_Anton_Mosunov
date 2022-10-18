from django.db import models


class OrderProduct(models.Model):
    order = models.ForeignKey(
        to='market.Order',
        verbose_name='Заказ',
        related_name='order',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='market.Product',
        verbose_name='Товар',
        related_name='product',
        on_delete=models.CASCADE
    )
    count = models.IntegerField(
        verbose_name='Остаток'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
