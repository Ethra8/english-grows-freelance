from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.individual_services, name= 'individual_services'),
    path('<int:service_id>/', views.pack_details, name= 'pack_details'),
    path('add_service/', views.add_service, name= 'add_service'),
    path('edit/<int:service_id>/', views.edit_service, name= 'edit_service'),
    path('delete/<int:service_id>/', views.delete_service, name= 'delete_service'),
]
