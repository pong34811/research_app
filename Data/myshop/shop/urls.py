from django.urls import path
from . import views

urlpatterns = [
    path('#add-shop', views.add_shop, name='add_shop'),
    path('shop-list/', views.shop_list, name='shop_list'),
]
