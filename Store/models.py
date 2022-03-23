from django.db import models
from category.models import *
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    product_description = models.TextField(max_length=500,blank=True)
    product_price = models.IntegerField()
    product_images = models.ImageField(upload_to='Photos/products')
    product_image1 = models.ImageField(upload_to='Photos/products',blank=True)
    product_image2 = models.ImageField(upload_to='Photos/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('Product',args=[self.category.slug,self.slug])


    def __str__(self):

        return self.product_name
