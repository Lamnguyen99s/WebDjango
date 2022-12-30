from django.urls import path
from . import views

urlpatterns = [
    path('<int:CategoryID>', views.getProductByCategory, name = 'List Product By Category'),
    path('detail/<int:ProductID>', views.getDetailProduct, name = 'Detail Product'),
]