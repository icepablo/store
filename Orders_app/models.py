from django.db import models
from Products_app.models import Product
from django.contrib.auth.models import User
class Order(models.Model):
    item_name=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
