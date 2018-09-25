from django.shortcuts import render, get_object_or_404

from Orders_app.models import Order
from Products_app.models import Product

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_order(request):
    orders = Order.objects.filter(customer__exact=request.user)
    length = len(orders)
    all_products = Order.objects.filter(customer__exact=request.user)

    summary_cost = 0
    for product in all_products:
        summary_cost += product.quantity * product.item_name.price

    if request.method == 'POST':
        order_id = request.POST['id']
        delete_order = get_object_or_404(Order, pk=order_id)
        product_object = get_object_or_404(Product, pk=delete_order.item_name.id)
        product_object.in_stock += delete_order.quantity
        delete_order.delete()
        product_object.save()

    return render(request, 'user_order.html', {'orders': orders, 'length': length, 'cost': summary_cost})
