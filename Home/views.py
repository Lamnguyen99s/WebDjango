from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from Category.models import Category
from Product.models import Product
from . models import Customer
from django.core.mail import send_mail
from django.views import View
# Create your views here.

def index(request):
    category = Category.objects.all()
    featuredproduct = Product.objects.all()[11:17]
    recentproduct = Product.objects.all()[:11]
    data = {
        'categories': category,
        'featuredproducts': featuredproduct,
        'recentproducts': recentproduct,
    }
    return render (request, 'Home/index.html', data)

def shop(request):
    shopProduct = Product.objects.all()
    data = {
        'shopProducts': shopProduct,
    }
    return render (request, 'Home/shop.html', data)

def detail(request):
    detailProduct = Product.objects.get(pk = 7)
    alsoProduct = Product.objects.all()[11:17]
    data = {
        'detailProduct' : detailProduct,
        'alsoProduct' : alsoProduct,
    }
    return render(request, 'Home/detail.html', data)
def contact(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        message = request.POST['Message']
        send_mail(subject, message, 'leethon33s@gmail.com', [email])
        return render(request, 'Home/contact.html', {'name': name})
    return render(request, 'Home/contact.html', {})

def cart(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity - 1 
                else:
                    cart[product]  = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'Home/cart.html', data)

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
    products = Product.objects.all()
    request.session['cart'] = {}
    data = {
        'products': products
    }
    return render(request, 'Home/checkout.html', data)
    
def signup(request):
    if request.method == 'POST':
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        
        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register()
            return render (request, 'Home/index.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'Home/signup.html', data)
    return render (request, 'Home/signup.html')

