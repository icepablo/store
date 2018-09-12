import django_filters

from Products_app.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'item_category': ['exact'],
            'price': ['gt', 'lt'],
        }


