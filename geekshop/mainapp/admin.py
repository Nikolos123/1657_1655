from django.contrib import admin

# Register your models here.
from mainapp.models import Product, ProductCategories

admin.site.register(ProductCategories)
admin.site.register(Product)