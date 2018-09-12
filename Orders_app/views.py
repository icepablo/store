from django.shortcuts import render

from Orders_app.models import Order


def user_order(request):
    orders = Order.objects.filter(customer__exact=request.user)
    length = len(orders)
    all_products = Order.objects.filter(customer__exact=request.user)
    summary_cost = 0
    for product in all_products:
        summary_cost += product.quantity * product.item_name.price

    return render(request, 'user_order.html', {'orders': orders, 'length': length, 'cost': summary_cost})
