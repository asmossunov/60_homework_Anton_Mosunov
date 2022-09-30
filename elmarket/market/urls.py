from django.contrib import admin
from django.urls import path

from market.views.products import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('products/', index_view, name='index'),
]
