from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Product, Category, Cart
from accounts.models import Customer
from django.conf.global_settings import LANGUAGE_CODE


# Create your views here.



def index(request):
    context = {}
    return render(request, "index.html", context)


def blog(request):
    context = {}
    return render(request, "blog.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def checkout(request):
    context = {}
    return render(request, "checkout.html", context)


def blogDetails(request):
    context = {}
    return render(request, "blog-details.html", context)


def shopDetails(request):
    context = {}
    return render(request, "shop-details.html", context)


def shopGrid(request):
    context = {}
    return render(request, "shop-grid.html", context)


def shopingCart(request):
    context = {}
    return render(request, "shoping-cart.html", context)


def main(request):
    context = {}
    return render(request, "main.html", context)


def manager(request):
    products = Product.objects.all()
    category = Category.objects.all()
    customers = Customer.objects.all()
    carts = Cart.objects.all()


    context = {'products': products,
               'category': category,
               'customers': customers,
               'carts': carts
               }
    return render(request, "manager.html", context)


def createproduct(request):
    if request.method == 'POST':
        print("11111   !!!!!!!!!!!!!!!!!!!!!!!!!!!")
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        weight = request.POST['weight']

        print("22222   !!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # images = request.POST['images']
        if 'images' in request.FILES:
            images = request.FILES['images']
            print(images)
        else:
            images = ''
        category = Category.objects.get(id=request.POST['category'])
        Product.objects.create(name=name, price=price, description=description,
                               weight=weight, images=images, category=category)
        return redirect('manager')
    else:
        messages.success(request, f"Noto'g'ri kiritildi, Qaytadan urinib ko'ring!")
        return render(request, "create_products.html")