from django.shortcuts import render
from products.models import Product, Review

# Create your views here.

def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")

def  products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(request, "products/products.html", context={
            'products' : products
        })

def detail_view(request, **kwargs):
    if request.method == "GET":
        print(request.GET)
        product = Product.objects.get(id=kwargs['id'])
        reviews = Review.objects.filter()
        data ={
            'products': product
        }
        return render(request, 'products/detail.html', context=data)