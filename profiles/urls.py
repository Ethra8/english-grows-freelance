from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name= 'profile'),
    # Shows ONE specific order
    path('order/<order_number>/', views.order_detail, name='order_detail'),
    path('account_information/', views.account_information, name= 'account_information'),
    path('order_history/', views.order_history, name= 'order_history'),
]
