from django.contrib import admin
from Category.models import Category
from Product.models import Product
from . models import Customer
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
# username = lamnguyen, email = nguyentronglamtb99@gmail.com, password = Lamthon99@