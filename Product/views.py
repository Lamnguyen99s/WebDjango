from django.shortcuts import render
from Product.models import Product
# Create your views here.

def getProductByCategory(request, CategoryID):
    lstProduct = Product.objects.filter(categoryID = CategoryID)
    # lstProduct = Product.objects.all()
    data = {
        'lstProduct': lstProduct,
    }
    return render(request, 'Product/listProduct.html', data)

def getDetailProduct(request, ProductID):
    detail = Product.objects.get(pk = ProductID)
    return render(request, 'Product/detailProduct.html', {'detail':detail})