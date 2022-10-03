from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from market.models import Product, CategoryChoices, StateChoices

from market.forms import ProductForm, FindProductForm


def index_view(request):
    if request.method == 'GET':
        products = Product.objects.filter(state='ACTIVE').order_by('-product_category', 'product_name')
        find_form = FindProductForm()
        context = {
            'products': products,
            'find_form': find_form,
            'choices': CategoryChoices.choices
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
    product = Product.objects.filter(pk=pk).update(**form.cleaned_data)
    return redirect('product_detail', pk)


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'delete_confirm.html', context)


def confirm_delete(request, pk):
    Product.objects.filter(pk=pk).update(
        state=StateChoices.NOT_ACTIVE)
    return redirect('index')


def find_product_view(request):
    if request.method == 'GET':
        product_name = request.GET.get('product_name')
        products = Product.objects.filter(product_name=product_name)
        form = ProductForm()
        find_form = FindProductForm()
        context = {
            'answer': 'товар не найден!',
            'products': products,
            'choices': CategoryChoices.choices,
            'find_form': find_form,
            'form': form
        }
        if products:
            context.pop('answer')
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', context)
    return redirect('index')


def category_view(request, category):
    products = Product.objects.filter(product_category=category).order_by('product_name')
    find_form = FindProductForm()
    context = {
        'category': category,
        'choices': CategoryChoices.choices,
        'find_form': find_form,
        'products': products,
        'choices': CategoryChoices.choices,
    }
    return render(request, 'categories.html', context)
