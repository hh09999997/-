"""
🔗 إعداد التوجيه (URLs) لمشروع mglh

هذا الملف يربط بين صفحات لوحة الإدارة والتطبيقات الداخلية:
- account: لإدارة المستخدمين وتسجيل الدخول.
- shop: لعرض المجلات وإدارة المبيعات.
- dashboard: للتحكم والإحصاءات.

كما يتعامل مع الملفات الثابتة والإعلامية أثناء التطوير.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🧭 لوحة الإدارة
    path('admin/', admin.site.urls),

    # 👤 تطبيق الحسابات
    path('account/', include('account.urls')),

    # 🛍️ متجر المجلات — الصفحة الرئيسية للموقع
    path('', include('shop.urls')),

    # 📊 لوحة التحكم
    path('dashboard/', include('dashboard.urls')),
]

# ----------------------------------------------------------
# 🖼️ عرض الملفات الثابتة والإعلامية أثناء التطوير
# ----------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
