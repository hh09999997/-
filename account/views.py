from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# ✅ صفحة إنشاء حساب
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل دخول تلقائي بعد التسجيل
            messages.success(request, "تم إنشاء الحساب بنجاح ✅")
            return redirect("shop:home")  # إعادة للصفحة الرئيسية
    else:
        form = UserCreationForm()

    return render(request, "account/signup.html", {"form": form})


# ✅ صفحة تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "تم تسجيل الدخول بنجاح ✅")
                return redirect("shop:home")
    else:
        form = AuthenticationForm()

    return render(request, "account/login.html", {"form": form})
