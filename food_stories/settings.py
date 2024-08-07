"""
Django settings for food_stories project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nx9vrc2vuyjy-3u0myt9mk$5c@-=c0!3m1zrfs_qr8$v_(0uz6'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = int(os.environ.get("DEBUG", default=1))
PROD = not DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'drf_spectacular',
    'core',
    'accounts',
    'stories',
    'psycopg',
    'social_django',
    'rest_framework',
    'rest_framework_simplejwt',
    "corsheaders",
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'food_stories.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'food_stories.wsgi.application'


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "accounts.api.serialziers.UserTokenObtainSerialzier",
}

AUTHENTICATION_BACKENDS = [
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Spectacular Food API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

SOCIAL_AUTH_FACEBOOK_KEY = 1113176829978715        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '65f97ff7ddea6caae8c58ea272a7d380'  # App Secret

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = "78xvd96cy2lgg2"         # Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = "d4DRXVhx8fhZxAFA"  # Client Secret

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "FoodDB",
        'USER': "food_user",
        'PASSWORD': "pass12345",
        'HOST': 'localhost',
        'PORT': 5432
    }
}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("POSTGRES_DB", "FoodDB"),
            'USER': os.environ.get("POSTGRES_USER", "food_user"),
            'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "pass12345"),
            'HOST': os.environ.get("POSTGRES_HOST", 'localhost'),
            'PORT': os.environ.get("POSTGRES_PORT", 5432)
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('tr', 'Turkish'),
    ('az', 'Azerbaijan'),
    ('ru', 'Russian'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('az', 'tr', 'en', 'ru')

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
            BASE_DIR, 'static'
        ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL= 'accounts.User'

from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
     message_constants.DEBUG: 'alert-secondary', 
     message_constants.INFO: 'alert-info',
     message_constants.SUCCESS: 'alert-success',
     message_constants.WARNING: 'alert-warning',
     message_constants.ERROR: 'alert-error',

}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bakhtiyarorujov@gmail.com'
EMAIL_HOST_PASSWORD = 'khqc sukd xckz pzjw'
EMAIL_USE_TLS = True

CELERY_BROKER_URL = f"redis://localhost':6379"
CELERY_RESULT_BACKEND = f"redis://localhost':6379"