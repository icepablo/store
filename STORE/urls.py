from django.contrib import admin
from django.urls import path,include

import Products_app.views
import Orders_app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Products_app.views.home, name='home'),
    path('my_order/', Orders_app.views.user_order, name='user_order'),
    path('accounts/', include('Accounts_app.urls'), name='accounts'),
    path('home/add_to_cart/<product_id>/', Products_app.views.add_to_cart, name='add_to_cart'),
]
