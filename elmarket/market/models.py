from django.db import models
from django.db.models import TextChoices
from django.core.validators import MinValueValidator


# CHOICES = [('other', 'разное'),
#            ('televisions', 'телевизоры'),
#            ('refrigerators', 'холодильники'),
#            ('electric_kettles', 'электрочайники')
#            ]


class CategoryChoices(TextChoices):
    other = 'разное'
    televisions = 'телевизоры'
    refrigerators = 'холодильники'
    electric_kettles = 'электрочайники'


class StateChoices(TextChoices):
    ACTIVE = 'ACTIVE'
    NOT_ACTIVE = 'NOT_ACTIVE'


class Product(models.Model):
    product_name = models.CharField(verbose_name=' Товар', max_length=100, null=False)
    product_description = models.TextField(verbose_name='Описание товара',
                                           max_length=3000, null=False, blank=False)
    product_image = models.TextField(verbose_name='Изображение', max_length=3000,
                                     null=False, blank=False)
    product_category = models.CharField(verbose_name=' Товар', choices=CategoryChoices.choices,
                                        max_length=100, null=False, default=CategoryChoices.choices[0][1])
    state = models.CharField(verbose_name='Состояние', choices=StateChoices.choices,
                             max_length=100, default=StateChoices.ACTIVE)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    price = models.DecimalField(verbose_name='Стоимость', max_length=100, max_digits=7,
                                decimal_places=2)
    remains = models.IntegerField(verbose_name='Остаток', validators=[MinValueValidator(0)],
                                  max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.product_name} {self.product_description} {self.product_category} ' \
               f'{self.price} {self.remains} {self.created_at} {self.changed_at}'
