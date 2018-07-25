from Products_app.models import Product
import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'item_category':['exact'],
            'price': ['gt', 'lt'],
        }

    '''
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Product
        fields = ['price', 'release_date']
    '''
