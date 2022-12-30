from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Home'),
    path('shop/', views.shop, name = 'shop'),
    path('detail/', views.detail, name = 'detail'),
    path('contact/', views.contact, name = 'contact'),
    path('cart/', views.cart, name = 'cart'),
    path('signup/', views.signup, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
]