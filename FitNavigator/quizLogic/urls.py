from django.urls import path, include
from . import views

urlpatterns = [
    path('fitNavigator', views.quiz, name="fitNavigator")
]