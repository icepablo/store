from django.urls import path

import Accounts_app.views


urlpatterns = [
    path('signup', Accounts_app.views.signup, name='signup'),
    path('login', Accounts_app.views.login, name='login'),
    path('logout', Accounts_app.views.logout, name='logout'),

    ]
