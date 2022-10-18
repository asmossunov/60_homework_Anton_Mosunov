from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


from market.models import CategoryChoices

from market.models import Product, ProductInCart
from market.models.products import MinLengthValidator, max_length_validator

from market.models.orders import Order


class ProductForm(forms.ModelForm):
    # product_name = forms.CharField(max_length=200, required=True, label='Название товара',
    #                                widget=forms.TextInput({'class': 'form-input'}))
    # product_description = forms.CharField(max_length=2000, required=True, label='Описание товара',
    #                                       widget=widgets.Textarea(attrs={'rows': 3, 'cols': 23}))
    # product_image = forms.CharField(max_length=2000, required=True, label='Изображение товара')
    # product_category = forms.ChoiceField(choices=CategoryChoices.choices, label='Категория товара')
    # price = forms.DecimalField(required=True, label='Стоимость товара')
    # remains = forms.IntegerField(required=True, label='Остатки товара')
    product_name = forms.CharField(
        label='Название товара',
        validators=(MinLengthValidator(5), max_length_validator)
    )
    product_description = forms.CharField(
        label='Описание товара',
        widget=forms.Textarea
    )

    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_image',
                  'product_category', 'price', 'remains')
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-input'}),
            'product_description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

            }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class AddProductToCartForm(forms.ModelForm):
    count = forms.IntegerField(required=True, label='Введите кол-во')

    class Meta:
        model = ProductInCart
        fields = ('count',)
        widgets = {
            'count': forms.NumberInput(attrs={'style': 'width: 10px'}),
        }



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user_name', 'phone', 'address')

