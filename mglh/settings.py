from pathlib import Path

# ----------------------------------------------------------
# 📂 المسار الأساسي للمشروع
# ----------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------
# 🔐 مفاتيح الأمان
# ----------------------------------------------------------
SECRET_KEY = 'django-insecure-zx!sw56byy6@rz(aq+)0$i3su#rkhu0j%%9z6nqxr(xug-#0!h'
DEBUG = True
ALLOWED_HOSTS = []

# ----------------------------------------------------------
# 🧩 التطبيقات المثبتة
# ----------------------------------------------------------
INSTALLED_APPS = [
    # 🧱 تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌟 تطبيقات المشروع
    'account.apps.AccountConfig',
    'shop.apps.ShopConfig',
    'dashboard.apps.DashboardConfig',
]

# ----------------------------------------------------------
# ⚙️ الطبقات الوسيطة (Middleware)
# ----------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ دعم اللغة العربية
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------------------------------
# 📍 نظام عناوين URLs
# ----------------------------------------------------------
ROOT_URLCONF = 'mglh.urls'

# ----------------------------------------------------------
# 🎨 إعدادات القوالب Templates
# ----------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # ✅ مجلد القوالب الرئيسي
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ----------------------------------------------------------
# 🚀 WSGI
# ----------------------------------------------------------
WSGI_APPLICATION = 'mglh.wsgi.application'

# ----------------------------------------------------------
# 🗄️ قاعدة البيانات (SQLite أثناء التطوير)
# ----------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------------------------------------
# 🔐 التحقق من كلمات المرور
# ----------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------------------------------------------
# 🌍 اللغة والمنطقة الزمنية
# ----------------------------------------------------------
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ----------------------------------------------------------
# 🖼️ الملفات الثابتة والإعلامية
# ----------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # ✅ مجلد التطوير
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # ✅ مجلد جمع الملفات للنشر (collectstatic)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ----------------------------------------------------------
# 🧱 الإعداد الافتراضي
# ----------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
