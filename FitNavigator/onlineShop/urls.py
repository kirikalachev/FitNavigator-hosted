from django.urls import path, include
from . import views

urlpatterns = [
    path("onlineShop", views.shop, name="onlineShop"),
]