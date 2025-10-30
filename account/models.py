from django.db import models
from django.contrib.auth.models import User

# 🧍‍♂️ ملف شخصي للمستخدم (توسعة المستخدم الافتراضي)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    full_name = models.CharField(max_length=150, verbose_name="الاسم الكامل")
    bio = models.TextField(blank=True, null=True, verbose_name="نبذة عن المستخدم")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return self.full_name
