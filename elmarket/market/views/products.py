from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from market.models import Product, CategoryChoices




def index_view(request):
    if request.method == 'GET':
        # products = Product.objects.all()
        products = Product.objects.all().order_by('product_category', 'product_name')
        context = {
            'products': products,
        }
        return render(request, 'index.html', context)


def product_view(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        context = {
            'product': product,
            'choices': CategoryChoices.choices,
        }
        return render(request, 'product.html', context)
