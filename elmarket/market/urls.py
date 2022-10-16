from django.contrib import admin
from django.urls import path

from market.views.products_in_cart import CartView
from market.views.base import ProductsIndexView
from market.views.products import category_view, ProductCreateView, ProductView, \
    ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductsIndexView.as_view(), name='index'),
    path('products/', ProductsIndexView.as_view(), name='index'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/<int:pk>/add_product_in_cart', ProductsIndexView.as_view(), name='index_add'),
    path('products/<int:pk>/add_product_in_cart_detail', ProductView.as_view(), name='product_detail_add'),
    path('cart/', CartView.as_view(), name='cart_open'),
    # path('products/find/', find_product_view, name='find_product'),
    path('products/<str:category>', category_view, name='list_by_category'),

]
