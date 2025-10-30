from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.home, name='home'),
    path('magazines/', views.magazine_list, name='magazine_list'),
]
