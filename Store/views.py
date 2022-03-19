from django.shortcuts import render
from .models import *
from category.models import *

# Create your views here.


def HomePage(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()

    context ={
        'products':products
    }

    return render(request,'./Store/home.html',context)


def Products(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()

    context ={
        'products':products,
        'categories':categories
    }

    return render(request,'./Store/Products.html',context)


def ShoppingCart(request):

    return render(request,'./Store/Cart.html')

def Contact(request):

    return render(request,'./Store/Contact.html')


def About(request):

    return render(request,'./Store/About.html')


def ProductDetails(request):

    return render(request,'./Store/ProductDetails.html')


def PlaceOrder(request):

    return render(request,'./Store/PlaceOrder.html')