from django.shortcuts import render,get_object_or_404, redirect
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from Orders_app.models import Order
from Products_app.models import Product


def home(request):
    products=Product.objects
    products_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'home.html', {'products': products, 'filter': products_filter})


def search(request):
    products_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'search.html', {'filter': products_filter})


@login_required(login_url="/accounts/login")
def add_to_cart(request, product_id):
    if request.method == 'POST':
        print(product_id)
        product_object = get_object_or_404(Product, pk=product_id)
        user_object = User.objects.get(id=request.user.id)
        order_object = Order()

        if product_object.in_stock > 0:
            order_object.item_name = product_object
            order_object.customer = user_object
            order_object.save()
            product_object.in_stock -= 1
            product_object.save()

    return redirect('/home/')
