from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_price','stock','category','created_at','updated_at','is_available')
    prepopulated_fields={'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)