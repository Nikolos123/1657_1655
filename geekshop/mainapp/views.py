import os
import json

from django.conf import settings
from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page, never_cache
from django.views.generic import DetailView

from mainapp.models import Product,ProductCategories

MODULE_DIR = os.path.dirname(__file__)

def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)
    return  json.load(open(file_path, encoding='utf-8'))

def index(request):
    content = {
        'title': 'Geekshop'
    }
    return  render(request,'mainapp/index.html',content)

def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategories.objects.all()
            cache.set(key,link_category)
        return link_category
    else:
        return ProductCategories.objects.all()


def get_product(category,page):
    if category:
        if settings.LOW_CACHE:
            key = f'link_product{category}{page}'
            link_product = cache.get(key)
            if link_product is None:
                link_product = Product.objects.filter(category_id=category).select_related('category')
                cache.set(key, link_product)
            return link_product
        else:
            return Product.objects.filter(category_id=category).select_related('category')
    else:
        if settings.LOW_CACHE:
            key = 'link_product'
            link_product = cache.get(key)
            if link_product is None:
                link_product = Product.objects.all().select_related('category')
                cache.set(key,link_product)
            return link_product
        else:
            return Product.objects.all().select_related('category')

def get_product_(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)


# @cache_page(3600)
# @never_cache
def products(request,id_category=None,page=1):

    if id_category:
        products_ = Product.objects.filter(category_id=id_category).select_related()
        # products_ = get_product(id_category,page)
    else:
        products_ = get_product(None,None)

    pagination = Paginator(products_,per_page=6)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)
    content = {
        'title' : 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        # 'categories': get_link_category(),
        'products': product_pagination

    }


    return  render(request,'mainapp/products.html',content)


#

class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'


    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['product'] = get_product_(self.kwargs.get('pk'))
        return context