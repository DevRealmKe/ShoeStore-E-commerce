from django.shortcuts import render

# Create your views here.


def HomePage(request):

    return render(request,'./Store/home.html')


def Products(request):

    return render(request,'./Store/Products.html')


def ShoppingCart(request):

    return render(request,'./Store/Cart.html')

def Contact(request):

    return render(request,'./Store/Contact.html')


def About(request):

    return render(request,'./Store/About.html')


def ProductDetails(request):

    return render(request,'./Store/ProductDetails.html')