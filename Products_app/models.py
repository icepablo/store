from django.db import models


class Category(models.Model):
    category_name = models.TextField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.TextField()
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    price = models.IntegerField(default=None)
    in_stock = models.IntegerField(default=None)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name



