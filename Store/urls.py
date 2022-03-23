from django.urls import path
from  .views import  *

urlpatterns = [
    path('',HomePage,name='Home'),
    path('shop',Products,name='shop'),
    path('cart',ShoppingCart,name='shopping_cart'),
    path('contact',Contact,name='Contact'),
    path('about',About,name='About'),
    path('<slug:category_slug>/<slug:product_slug>',ProductDetails,name='Product'),
    path('place_order',PlaceOrder,name='Place_order'),

]