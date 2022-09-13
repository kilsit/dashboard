from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('order/', views.order, name="order"),
    path('staff/', views.staff, name="staff"),
    path('staff_index/', views.index, name="staff_index"),
    path('product/', views.product, name="product"),
    path('product/delete/<int:pk>/', views.product_delete, name="dashboard-product_delete"),
    path('product/update/<int:pk>/', views.product_update, name="dashboard-product_update"),
   
]


