from django.db.models import Q
from django.shortcuts import render
from urllib.parse import urlencode
from django.views.generic import ListView
from market.models import Product


from market.forms import SearchForm
from market.models import CategoryChoices


# def index_view(request):
#     if request.method == 'GET':
#         products = Product.objects.filter(is_deleted=False).order_by('-product_category', 'product_name')
#         find_form = FindProductForm()
#         context = {
#             'products': products,
#             'find_form': find_form,
#             'choices': CategoryChoices.choices
#         }
#         return render(request, 'index.html', context)

class ProductsIndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-created_at',)
    paginate_by = 4
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(product_name__icontains=self.search_value) | Q(product_description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsIndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
