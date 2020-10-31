from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,default='')
    subcategory = models.ForeignKey(
        SubCategory,on_delete=models.CASCADE,default='')
    description = models.CharField(max_length=200, default='',null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
