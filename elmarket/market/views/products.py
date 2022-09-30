from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from market.models import Product, CategoryChoices

from market.forms import ProductForm, CHOICES


def index_view(request):
    if request.method == 'GET':
        # products = Product.objects.all()
        products = Product.objects.all().order_by('product_category', 'product_name')
        context = {
            'products': products,
            'choices': CHOICES
        }
        return render(request, 'index.html', context)


def product_view(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=pk)
        context = {
            'product': product,
            'choices': CHOICES,
        }
        return render(request, 'product.html', context)

def add_product_view(request):
    form = ProductForm()
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'add_product.html', context)
    form = ProductForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'add_product.html', context)
    product = Product.objects.create(**form.cleaned_data)
    return redirect('product_detail', pk=product.pk)


def edit_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        print(product.product_category)
        form = ProductForm(initial={
            'product_name': product.product_name,
            'state': product.state,
            'product_description': product.product_description,
            'product_image': product.product_image,
            'product_category': product.product_category,
            'price': product.price,
            'remains': product.remains
        })
        return render(request, 'edit_product.html', context={'form': form, 'product': product})
    form = ProductForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form,
            'product': product
        }
        return render(request, 'edit_product.html', context)
    task = Product.objects.create(**form.cleaned_data)
    return redirect('product_detail', pk=task.pk)
