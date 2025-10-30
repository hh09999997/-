from django.shortcuts import render
from .models import Magazine

def home(request):
    return render(request, 'shop/home.html')  # ✅ الصفحة الرئيسية

def magazine_list(request):
    magazines = Magazine.objects.all()  # ✅ جلب كل المجلات
    return render(request, 'shop/magazine_list.html', {'magazines': magazines})
