from django.shortcuts import render
from django.http import HttpResponse
from .models import  Product


# Create your views here.
def index(request):
    #pro=Product.get_all_products();

    return render(request , 'thewayshop/index.html')#, {'products' : pro})
