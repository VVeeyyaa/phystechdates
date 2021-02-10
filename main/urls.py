from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.profile),
    path('home', views.index),
    path('drink', views.drink),
]
