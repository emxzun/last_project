from django.contrib import admin

from product.models import Product, Category

admin.site.register(Category)
admin.site.register(Product)
