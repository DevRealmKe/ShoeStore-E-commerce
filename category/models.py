from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.CharField(max_length=255,blank=True)
    category_image = models.ImageField(upload_to='Photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



    def __str__(self):
        return self.category_name



class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'sub category'
        verbose_name_plural = 'sub categories'



    def __str__(self):
        return self.subcategory_name

