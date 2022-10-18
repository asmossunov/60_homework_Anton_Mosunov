from django.contrib import admin
from market.models import ProductInCart
from market.models import Product
from market.models import Order
from market.models import OrderProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description', 'product_category', 'price', 'remains', 'changed_at', 'created_at')
    list_filter = ('id', 'product_name', 'product_description', 'product_category', 'price', 'remains', 'changed_at', 'created_at')
    search_fields = ('id', 'product_name', 'product_description', 'product_category', 'price', 'remains', 'changed_at', 'created_at')
    fields = ('id', 'product_name', 'product_description', 'product_category', 'product_image', 'price', 'remains')
    readonly_fields = ['id']


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'count', 'changed_at', 'created_at')
    list_filter = ('id', 'product', 'count', 'changed_at', 'created_at')
    search_fields = ('id', 'product', 'count', 'changed_at', 'created_at')
    fields = ('id', 'product', 'count')
    readonly_fields = ['id']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'phone', 'address', 'created_at', 'updated_at')
    list_filter = ('id', 'user_name', 'phone', 'address', 'created_at', 'updated_at')
    search_fields = ('id', 'user_name', 'phone', 'address', 'created_at', 'updated_at')
    fields = ('id', 'user_name', 'phone', 'address')
    readonly_fields = ['id']


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'order_id', 'product_id', 'created_at')
    list_filter = ('id', 'count', 'order_id', 'product_id', 'created_at')
    search_fields = ('id', 'count', 'order_id', 'product_id', 'created_at')
    fields = ('id', 'count', 'order_id', 'product_id')
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInCart, ProductInCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
