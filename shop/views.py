from django.shortcuts import render
from .models import Magazine  # استيراد الموديل

# ✅ الصفحة الرئيسية - تعرض المنتجات
def home(request):
    magazines = Magazine.objects.all()  # جلب جميع المجلات من قاعدة البيانات
    return render(request, 'shop/home.html', {'magazines': magazines})
