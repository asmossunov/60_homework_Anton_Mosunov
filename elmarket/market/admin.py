from django.contrib import admin
from market.models import ProductInCart
from market.models import Product


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


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInCart, ProductInCartAdmin)
