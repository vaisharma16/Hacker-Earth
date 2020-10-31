from django.contrib import admin
from .models import Product
from .models import Category
from .models import SubCategory

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category','description']

class CategoryProduct(admin.ModelAdmin):
    list_display = ['name']

class SubCategoryProduct(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.

admin.site.register(Product,AdminProduct)
admin.site.register(Category,CategoryProduct)
admin.site.register(SubCategory,SubCategoryProduct)