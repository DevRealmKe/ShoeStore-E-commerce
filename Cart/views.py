from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from Store.models import *




# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()

    return cart

# def ShoppingCart(request):
#     return render(request, 'Store/Cart.html')


def AddToCart(request,product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id= _cart_id(request)
        )

    cart.save()


    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,cart=cart,quantity=1)

        cart_item.save()

   
    return redirect('cart:cart_page')


def remove_to_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart:cart_page')

def DeleteCartItem(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    cart_item = CartItem.objects.get(product=product,cart=cart)

    cart_item.delete()

    return redirect('cart:cart_page')

def ShoppingCart(request,total=0,quantity=0,cart_item=None):
    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)

        for cart_item in cart_items:
            total +=(cart_item.product.product_price * cart_item.quantity)
            quantity += cart_item.quantity
        tax =(3*100)
        grandtotal =total + tax
    except ObjectNotExist:
        pass

    context = {
        'total':total,
        'grandtotal':grandtotal,
        'tax':tax,
        'quantity':quantity,
        'cart_items':cart_items
        }
    return render(request, 'Store/Cart.html',context)