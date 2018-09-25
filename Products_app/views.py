from django.shortcuts import render, get_object_or_404, redirect
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from Orders_app.models import Order
from Products_app.models import Product

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    if request.method == 'POST':
        object_id = request.POST['id']
        product_object = get_object_or_404(Product, pk=object_id)
        sign = request.POST['sign']

        if sign == 'plus':
            if product_object.quantity < product_object.in_stock:
                product_object.quantity += 1
                product_object.save()

        elif sign == 'minus':
            if product_object.quantity > 1:
                product_object.quantity -= 1
                product_object.save()

    products_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    movies = Product.objects.filter(item_category__category_name__icontains='filmy')
    games = Product.objects.filter(item_category__category_name__icontains='gry')
    books = Product.objects.filter(item_category__category_name__icontains='książki')
    return render(request, 'home.html', {'games': games, 'movies': movies, 'books': books, 'filter': products_filter})


@login_required(login_url="/accounts/login")
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product_object = get_object_or_404(Product, pk=product_id)
        user_object = User.objects.get(id=request.user.id)
        order_object = Order()
        orders_filter = Order.objects.values('item_name', 'id').filter(customer__exact=user_object)

        def make_order():
            order_object.item_name = product_object
            order_object.customer = user_object
            order_object.quantity = product_object.quantity
            order_object.save()
            product_object.in_stock -= product_object.quantity
            product_object.quantity = 1
            product_object.save()

        if product_object.in_stock > 0:
            if orders_filter:
                for product in orders_filter:
                    if product['item_name'] == product_object.id:
                        add_to_order = get_object_or_404(Order, pk=product['id'])
                        add_to_order.quantity += product_object.quantity
                        add_to_order.save()
                        product_object.in_stock -= product_object.quantity
                        product_object.quantity = 1
                        product_object.save()
                    else:
                        make_order()
            else:
                make_order()



    return redirect('/home/')
