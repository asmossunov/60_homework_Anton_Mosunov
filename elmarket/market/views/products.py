from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from market.models import Product, CategoryChoices

from market.forms import ProductForm

from market.forms import AddProductToCartForm

from market.models import ProductInCart

from market.forms import SearchForm


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductView(DetailView):
    template_name = 'product.html'
    model = Product
    answer = None

    def get(self, request, *args, **kwargs):
        self.product_to_cart_form = AddProductToCartForm(self.request.GET)
        self.product_to_cart_value = self.get_product_to_cart()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.product_to_cart_form = AddProductToCartForm(self.request.POST)
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

    def get_product_to_cart(self):
        if self.product_to_cart_form.is_valid():
            return self.product_to_cart_form.cleaned_data.get('count')
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        # queryset = self.get_queryset()
        context = super(ProductView, self).get_context_data(object_list=object_list, **kwargs)
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        context['product_to_cart_form'] = self.product_to_cart_form
        context['choices'] = CategoryChoices.choices
        context['product'] = product
        context['answer'] = self.answer
        return context


class ProductCreateView(SuccessDetailUrlMixin, CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    model = Product


class ProductUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'edit_product.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    template_name = 'delete_confirm.html'
    model = Product
    success_url = reverse_lazy('index')


def category_view(request, category):
    products = Product.objects.filter(product_category=category).order_by('product_name')
    find_form = SearchForm()
    context = {
        'category': category,
        'choices': CategoryChoices.choices,
        'find_form': find_form,
        'products': products,
    }
    return render(request, 'categories.html', context)


