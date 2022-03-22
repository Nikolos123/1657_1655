from django.shortcuts import render

# Create your views here.

def index(request):

    return  render(request,'mainapp/index.html')


def products(request):

    return  render(request,'mainapp/products.html')


# def test(request):
#     context = {'title':'geekshop',
#                'header':'Welcome',
#                'user':'Nikolay',
#                'products': [
#                     {'name':'Худи черного цвета с монограммами adidas Originals','price':6090},
#                     {'name':'Синяя куртка The North Face','price':23725},
#                     {'name':'Коричневый спортивный oversized-топ ASOS DESIGN','price':3390},
#                     {'name':'Черный рюкзак Nike Heritage','price':2340},
#                     {'name':'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex','price':13590},
#                     {'name':'Темно-синие широкие строгие брюки ASOS DESIGN','price':2890}
#                ],
#                'promotion':False,
#
#                'products_promotion': [
#                    {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 50},
#                    {'name': 'Синяя куртка The North Face', 'price': 50},
#                    {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 50},
#                    {'name': 'Черный рюкзак Nike Heritage', 'price': 50},
#                    {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 50},
#                    {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 50}
#                ],
#                }
#
#
#     return  render(request,'mainapp/test.html',context)