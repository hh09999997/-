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
    # 🧭 لوحة الإدارة الافتراضية
    path('admin/', admin.site.urls),

    # 🧍‍♂️ تطبيق الحسابات (Account)
    path('account/', include('account.urls')),

    # 🛍️ تطبيق المتجر والمجلات (Shop)
    path('', include('shop.urls')),  # الصفحة الرئيسية للمتجر

    # 📊 تطبيق لوحة التحكم (Dashboard)
    path('dashboard/', include('dashboard.urls')),
]

# ----------------------------------------------------------
# 🖼️ دعم عرض الملفات الثابتة والإعلامية أثناء التطوير
# ----------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
