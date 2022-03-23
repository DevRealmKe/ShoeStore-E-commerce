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

def ProductDetails(request,category_slug,product_slug):
    all_products = Product.objects.all()
    try:
        single_product =Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product':single_product,
        'all_products':all_products
    }

    return render(request,'./Store/ProductDetails.html',context)


def ShoppingCart(request):

    return render(request,'./Store/Cart.html')

def Contact(request):

    return render(request,'./Store/Contact.html')


def About(request):

    return render(request,'./Store/About.html')





def PlaceOrder(request):

    return render(request,'./Store/PlaceOrder.html')