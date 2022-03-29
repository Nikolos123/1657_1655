import os
import json

from django.shortcuts import render

# Create your views here.
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


def products(request):

    products = read_file('fixtures/goods.json')
    categories = read_file('fixtures/categories.json')

    content = {
        'title' : 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all()
    }


    return  render(request,'mainapp/products.html',content)


#

