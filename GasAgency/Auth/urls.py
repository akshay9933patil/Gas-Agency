# customer_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register_customer/', views.register_customer, name='register_customer_url'),
    path('register_customer_representative/', views.register_customer_representative, name='register_customer_representative'),
    path('login_customer/', views.customer_login_view, name='login_customer_url'),
    path('login_customer_representative/', views.customer_representative_login_view, name='login_customer_representative_url'),
    path('logout/', views.user_logout, name='logout_url'),
]
