from django.contrib import admin
from django.urls import path

from market.views.products import index_view, category_view, find_product_view, product_view, add_product_view, edit_product_view, delete_view, confirm_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('products/', index_view, name='index'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('products/add/', add_product_view, name='product_add'),
    path('products/<int:pk>/edit/', edit_product_view, name='product_edit'),
    path('products/<int:pk>/delete/', delete_view, name='product_delete'),
    path('products/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
    path('products/find/', find_product_view, name='find_product'),
    path('products/<str:category>', category_view, name='list_by_category'),

]
