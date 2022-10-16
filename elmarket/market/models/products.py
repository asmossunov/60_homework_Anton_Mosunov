from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import TextChoices

from django.core.validators import BaseValidator, MinValueValidator
from django.utils.deconstruct import deconstructible


class CategoryChoices(TextChoices):
    OTHER = 'other', 'разное'
    TELEVISIONS = 'televisions', 'телевизоры'
    REFRIGERATORS = 'refrigerators', 'холодильники'
    ELECTRIC_KETTLES = 'electric_kettles', 'электрочайники'


class Product(models.Model):
    product_name = models.CharField(verbose_name=' Товар', max_length=100, null=False)
    product_description = models.TextField(verbose_name='Описание товара',
                                           max_length=3000, null=False, blank=True)
    product_image = models.CharField(verbose_name='Изображение', max_length=3000,
                                     null=False, blank=False)
    product_category = models.CharField(verbose_name=' Товар', choices=CategoryChoices.choices,
                                        max_length=100, null=False, default=CategoryChoices.OTHER)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    price = models.DecimalField(verbose_name='Стоимость', max_length=100, max_digits=7,
                                decimal_places=2)
    remains = models.IntegerField(verbose_name='Остаток', validators=[MinValueValidator(0)],
                                  null=False, blank=False)

    def __str__(self):
        return f'{self.product_name} {self.product_description} {self.product_category} ' \
               f'{self.price} {self.remains} {self.created_at} {self.changed_at}'


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Введённое значение "%(value) s" имеет длину %(show_value) d! ' \
              'Должно состоять не чем из %(limit_value) d символов'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)

@deconstructible
def max_length_validator(string):
    if len(string) > 200:
        raise ValidationError("Превышена максимальная длина строки 200 символов")
    return string
