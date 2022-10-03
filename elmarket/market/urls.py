from django.contrib import admin
from django.urls import path

from market.views.products import index_view, product_view, add_product_view, edit_product_view, delete_view, confirm_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('products/', index_view, name='index'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('products/add/', add_product_view, name='product_add'),
    path('products/<int:pk>/edit/', edit_product_view, name='product_edit'),
    path('task/<int:pk>/delete/', delete_view, name='product_delete'),
    path('task/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
]
