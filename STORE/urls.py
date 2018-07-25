"""STORE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import Products_app.views
import Orders_app.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Products_app.views.home,name='home'),
    path('my_order/',Orders_app.views.user_order,name='user_order'),
    path('accounts/',include('Accounts_app.urls'),name='accounts'),
    path('search/', Products_app.views.search,name='search'),
    path('home/borrow',Products_app.views.borrow,name='borrow'),
]
