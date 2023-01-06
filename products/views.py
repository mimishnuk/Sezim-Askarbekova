from django.shortcuts import render, redirect
from products.models import Product, Review, Categori
from products.forms import ProductCreateForm, ReviewCreateForm

# Create your views here.

PAGINTIONS_LIMIT = 6

def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")


def products_view(request):
    if request.method == 'GET':
        categories_id = int(request.GET.get("category_id", 0))
        search = request.GET.get("Search")
        page = int(request.GET.get("page", 1))

        if categories_id:
            products = Product.objects.filter(category__in=[categories_id])
        else:
            products = Product.objects.all()

        if search:
            products = products.filter(title__icontains=request.GET.get('Search'))

        max_page = products.__len__() / PAGINTIONS_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1

        products = products[PAGINTIONS_LIMIT * (page - 1): PAGINTIONS_LIMIT * page]

        return render(request, 'products/products.html', context={
            'products': products,
            'user': None if request.user.is_anonymous else request.user,
            'max_page': range(1, round(max_page) + 1)
        })


def detail_view(request, **kwargs):
    if request.method == "GET":
        print(request.GET)
        product = Product.objects.get(id=kwargs['id'])
        reviews = Review.objects.filter()
        data ={
            'products': product,
            'review_form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=data)

    if request.method == 'POST':
        products = Product.objects.get(id=id)
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                author=request.user,
                products_id=id,
                text=form.cleaned_data.get('text'),
                commentable=form.cleaned_data.get('commentable', True)
            )

            return redirect(f'/products/{id}/')

        else:
            return render(request, 'products/detail.html', context={
            'products': products,
            'review_form': form,

        })



def categories_view(request):
    if request.method == "GET":
        categories = Categori.objects.all()
        return render(request, "categories/index.html", context={
            'categories': categories
        })

def product_create_view(request, **kwargs):
    if request.method == "GET":
        return render(request, 'products/create.html', context={
            'form': ProductCreateForm
        })
    if request.method == "POST":
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():

            Product.objects.create(
                author=request.user,
                name=request.POST.get('name'),
                discription=request.POST.get('discription'),
                price=request.POST.get('price', 0),
                rate=request.POST.get('rate', 1)

            )
            return redirect(f"/products/")

        else:
            return render(request, 'products/create.html', context={
                'form': form
            })


