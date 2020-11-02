from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=150, db_index=True)

    @staticmethod
    def get_subcategories(category_id):
        if category_id:
            return SubCategory.objects.filter(category = category_id)

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

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();
