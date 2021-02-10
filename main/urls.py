from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('profile/', include('user_profile.urls')),
    path('', views.index, name="home"),
    path('drink', views.drink),
]
