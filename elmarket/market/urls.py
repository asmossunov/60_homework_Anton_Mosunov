from django.contrib import admin
from django.urls import path

from market.views.products import index_view, product_view, add_product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('products/', index_view, name='index'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('tasks/add/', add_product_view, name='product_add'),
]
