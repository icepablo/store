from django.shortcuts import render

from Orders_app.models import Order


def user_order(request):
    orders = Order.objects.filter(customer__exact=request.user)
    length = len(orders)
    return render(request, 'user_order.html', {'orders': orders, 'length': length})
