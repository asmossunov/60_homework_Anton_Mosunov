from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from urllib.parse import urlencode

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from market.models import Product


from market.forms import SearchForm, AddProductToCartForm
from market.models import CategoryChoices

from market.models import ProductInCart


class ProductsIndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-product_category', 'product_name')
    paginate_by = 6
    paginate_orphans = 0
    answer = None

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.product_to_cart_form = AddProductToCartForm(self.request.GET)
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.product_to_cart_form = AddProductToCartForm(self.request.POST)
        self.search_value = self.get_search_value()
        self.product_to_cart_value = self.get_product_to_cart()
        if self.product_to_cart_value:
            product_id = self.kwargs.get('pk')
            count = self.product_to_cart_value
            product = Product.objects.get(id=product_id)
            if product.remains >= count:
                if ProductInCart.objects.filter(product=product).exists():
                    product_in_cart = ProductInCart.objects.get(product_id=product_id)
                    counter = product_in_cart.count + count
                    ProductInCart.objects.filter(product_id=product_id).update(count=counter)
                else:
                    ProductInCart.objects.create(product_id=product_id, count=count)
            else:
                self.answer = 'Такое количество товара отсутствует на складе.' \
                              ' Введите меньшее значение.'
            return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_product_to_cart(self):
        if self.product_to_cart_form.is_valid():
            return self.product_to_cart_form.cleaned_data.get('count')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True, remains__lt='1')
        if self.search_value:
            query = Q(product_name__icontains=self.search_value) | Q(product_description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsIndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['product_to_cart_form'] = self.product_to_cart_form
        context['choices'] = CategoryChoices.choices
        context['answer'] = self.answer
        return context
