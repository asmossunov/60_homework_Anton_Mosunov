from django.db import models


class ProductInCart(models.Model):
    product = models.ForeignKey(
        to='market.Product',
        verbose_name='Статус',
        related_name='products_in_cart',
        on_delete=models.CASCADE
    )
    count = models.IntegerField(
        verbose_name='Количество'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.product} {self.count}'

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def total(self):
        return self.count * self.product.priсe
