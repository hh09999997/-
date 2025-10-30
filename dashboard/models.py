from django.db import models

# 📊 نموذج افتراضي (placeholder)
# يتم استخدام هذا التطبيق للعرض والتحليلات فقط غالبًا
class DashboardLog(models.Model):
    action = models.CharField(max_length=100, verbose_name="الإجراء")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "سجل لوحة التحكم"
        verbose_name_plural = "سجلات لوحة التحكم"

    def __str__(self):
        return self.action
