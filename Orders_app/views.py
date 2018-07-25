from django.shortcuts import render
from Orders_app.models import Order
from django.contrib.auth.models import User
# Create your views here.
def user_order(request):
    orders=Order.objects.filter(customer__exact=request.user)
    length=len(orders)
    return render(request, 'user_order.html',{'orders':orders,'length':length})
