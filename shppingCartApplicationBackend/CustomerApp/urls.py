from django.urls import path
# from .views import CustomerProfile

# from . import views

# customer = CustomerProfile.as_view()
from CustomerApp.views.auth import (RegisterUser, LoginUser)

urlpatterns = [
    path("auth/register", RegisterUser.as_view(), name="auth-register"),
    path("auth/login", LoginUser.as_view(), name="auth-login"),
    # path('customer-insert/',customer, name='insert_customer'),
    # path('get-all-customer/',customer, name='get_all_customer'),
    # path('update-customer/<str:customer_id>',customer,name='update_customer'),
    # path('delete-customer/<str:customer_id>',customer, name='delete_customer')
]
