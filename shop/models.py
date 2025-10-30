from django.db import models
from cloudinary.models import CloudinaryField

# 📂 تصنيفات المجلات
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


# 📚 مجلة
class Magazine(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="التصنيف"
    )
    title = models.CharField(max_length=150, verbose_name="عنوان المجلة")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="السعر")

    # ✅ غلاف من Cloudinary
    cover = CloudinaryField(
        'صورة الغلاف',
        folder='magazines/covers/',
        blank=True,
        null=True
    )

    # ✅ فيديو من Cloudinary
    preview_video = CloudinaryField(
        'فيديو تعريفي',
        folder='magazines/videos/',
        resource_type='video',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "مجلة"
        verbose_name_plural = "المجلات"

    def __str__(self):
        return self.title
