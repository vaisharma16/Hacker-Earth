from django.shortcuts import render
from django.http import HttpResponse
from .models import  Product
from .models import  Category
from .models import  SubCategory


# Create your views here.
def index(request):
    #pro=Product.get_all_products();
    categories=Category.get_all_categories()
    categoryID=request.GET.get('category')
    subcategories = SubCategory.get_subcategories(categoryID)
    #if categoryID:
        #products=Product.get_all_products_by_categoryid(categoryID)
        #subcategories = SubCategory.get_subcategories(categoryID)
    #else:

        #subcategories=Product.get_all_products()
    data={}
    #data['products']=products
    data['categories']=categories
    data['subcategories'] = subcategories
    return render(request , 'thewayshop/index.html', data)
