from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


from market.models import CategoryChoices


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=200, required=True, label='Название товара',
                                   widget=forms.TextInput({'class': 'form-input'}))
    product_description = forms.CharField(max_length=2000, required=True, label='Описание товара',
                                          widget=widgets.Textarea)
    product_image = forms.CharField(max_length=2000, required=True, label='Изображение товара')
    product_category = forms.ChoiceField(choices=CategoryChoices.choices, label='Категория товара')
    price = forms.DecimalField(required=True, label='Стоимость товара')
    remains = forms.IntegerField(required=True, label='Остатки товара')

    def clean_task_text(self):
        task_text = self.cleaned_data.get('task_text')
        if len(task_text) < 2:
            raise ValidationError('Поле должно быть заполнено более чем одним символом')
        return task_text
