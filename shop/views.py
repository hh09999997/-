from django.shortcuts import render
from .models import Magazine

# ✅ الصفحة الرئيسية — تعرض المجلات
def home(request):
    magazines = Magazine.objects.all()
    return render(request, 'shop/home.html', {'magazines': magazines})

# ✅ صفحة قائمة المجلات
def magazine_list(request):
    magazines = Magazine.objects.all()
    return render(request, 'shop/magazine_list.html', {'magazines': magazines})
