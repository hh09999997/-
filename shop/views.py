from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')  # ✅ يعرض الصفحة مع الهيدر والفوتر
