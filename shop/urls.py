from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.home, name='home'),
]


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
