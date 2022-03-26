from django.urls import path
from .views import *

app_name = 'Cart'

urlpatterns = [
    path('',ShoppingCart,name='cart_page'),
    path('add_to_cart/<int:product_id>/',AddToCart,name='add_to_cart'),
    path('remove_to_cart/<int:product_id>/',remove_to_cart,name='remove_to_cart'),
    path('delete_cart_item/<int:product_id>/',DeleteCartItem,name='delete_cart_item'),
]