from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from market.forms import AddProductToCartForm

from market.models import ProductInCart

from market.models import Product

from market.models import CategoryChoices

from market.forms import OrderForm


#
# class AddProductToCartView(CreateView):
#
#     template_name = 'test.html'
#     form_class = AddProductToCartForm
#     model = ProductInCart
#
#     def form_valid(self, form):
#         product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
#         form.instance.product = product
#         # form.instance.count = AddProductToCartForm(self.request.GET)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('product_detail', kwargs={'pk': self.object.product_id})


class CartView(ListView):
    template_name = 'cart/cart.html'
    model = ProductInCart
    context_object_name = 'products'
    extra_context = CategoryChoices.choices

    def get(self, request, *args, **kwargs):
        self.order_form = OrderForm(self.request.GET)
        self.product_to_cart_value = self.get_product_to_cart()
        return super().get(request, *args, **kwargs)


    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_product_to_cart(self):
        if self.product_to_cart_form.is_valid():
            return self.product_to_cart_form.cleaned_data.get('count')
        return None

    def total(self):
        return self.product.priсe * self.count

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartView, self).get_context_data(object_list=object_list, **kwargs)
        products = ProductInCart.objects.all()
        total = 0
        for product in products:
            total += product.product.price * product.count
        context['total'] = total
        context['products'] = ProductInCart.objects.all()
        return context



