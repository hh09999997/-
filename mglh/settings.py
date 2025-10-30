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
    # 🧱 تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌟 تطبيقات المشروع الداخلية
'account.apps.AccountConfig',
'shop.apps.ShopConfig',
'dashboard.apps.DashboardConfig',
]

# ----------------------------------------------------------
# ⚙️ الطبقات الوسيطة (Middlewares)
# ----------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ لدعم اللغة العربية
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------------------------------
# 📍 إعدادات التوجيه (URLs)
# ----------------------------------------------------------
ROOT_URLCONF = 'mglh.urls'

# ----------------------------------------------------------
# 🎨 إعدادات القوالب (Templates)
# ----------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ المجلد الرئيسي للقوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ----------------------------------------------------------
# 🚀 تطبيق WSGI
# ----------------------------------------------------------
WSGI_APPLICATION = 'mglh.wsgi.application'

# ----------------------------------------------------------
# 🗄️ قاعدة البيانات (SQLite لتجارب التطوير)
# ----------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------------------------------------
# 🔐 تحقق كلمات المرور
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
LANGUAGE_CODE = 'ar'              # ✅ اللغة العربية
TIME_ZONE = 'Asia/Riyadh'         # ✅ التوقيت المحلي للرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ----------------------------------------------------------
# 🖼️ الملفات الثابتة والإعلامية
# ----------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ----------------------------------------------------------
# 🧱 الإعداد الافتراضي للمفاتيح الأساسية
# ----------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
