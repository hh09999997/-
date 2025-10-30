from django.db import models

# 🧾 سجل أحداث لوحة التحكم
class DashboardLog(models.Model):
    action = models.CharField(max_length=100, verbose_name="الإجراء")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "سجل لوحة التحكم"
        verbose_name_plural = "سجلات لوحة التحكم"

    def __str__(self):
        return f"{self.action} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
