from django.shortcuts import redirect

from django.views.generic import CreateView, ListView, DeleteView

from market.models import ProductInCart

from market.models import Product

from market.models import CategoryChoices

from market.forms import OrderForm

from market.models import Order

from market.models import OrderProduct




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
                product_from = Product.objects.get(id=product.product_id)
                order_product = OrderProduct.objects.create(
                    order=order,
                    product=product_from,
                    count=product.count
                )
                new_level = product_from.remains - product.count
                Product.objects.filter(id=product_from.id).update(remains=new_level)
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
