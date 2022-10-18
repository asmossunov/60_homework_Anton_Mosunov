from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from market.forms import AddProductToCartForm

from market.models import ProductInCart

from market.models import Product

from market.models import CategoryChoices

from market.forms import OrderForm

from market.models import Order

from market.models import OrderProduct


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
        self.order_value = self.get_order_value()
        return super().get(request, *args, **kwargs)

    def get_order_value(self):
        if self.order_form.is_valid():
            return self.order_form.cleaned_data
        return None

    # def form_valid(self, form):
    #     form.instance.user_name = self.kwargs['user_name']
    #     form.instance.phone = self.kwargs['phone']
    #     form.instance.user_name = self.kwargs['address']
    #     return super(CartView, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartView, self).get_context_data(object_list=object_list, **kwargs)
        products = ProductInCart.objects.all()
        total = 0
        for product in products:
            total += product.product.price * product.count
        context['order_form'] = self.order_form
        context['total'] = total
        context['products'] = ProductInCart.objects.all()
        return context


class OrderCreateView(CreateView):
    model = Order

    def post(self, request, *args, **kwargs):
        self.order_form = OrderForm(self.request.POST)
        if self.order_form.is_valid():
            products_from_cart = ProductInCart.objects.all()
            order = Order.objects.create(**self.order_form.cleaned_data)
            for product in products_from_cart:
                print(product.id)
                product_from = Product.objects.get(id=product.product_id)
                print(product_from)
                order_product = OrderProduct.objects.create(
                    order=order,
                    product=product_from,
                    count=product.count
                )
        products = ProductInCart.objects.all()
        products.delete()
        return redirect('index')


class CartProductDeleteView(DeleteView):
    model = ProductInCart

    def post(self, request, *args, **kwargs):
        print(kwargs['pk'])
        product = ProductInCart.objects.filter(pk=kwargs['pk'])
        product.delete()
        return redirect('cart_open')
