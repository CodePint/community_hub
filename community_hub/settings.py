"""
Django settings for community_hub project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*-m&r!cw0dy!t)tfddwj)(cd!0k7bmm%w@4d!c98t4hi@zhv-x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    ## django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    ## custom apps
    # all_auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # extensions
    'django_extensions',

    ## project apps
    'blog',
    'pages',
    'users',
    'helpme'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'community_hub.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR,"community_hub/templates")
ALLAUTH_TEMPLATE_DIR = os.path.join(TEMPLATE_DIR, "allauth")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ALLAUTH_TEMPLATE_DIR],
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

WSGI_APPLICATION = 'community_hub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'community_db',
        'USER': 'hub_admin',
        'PASSWORD': 'HxHH4GEmqwmikKnaTdG',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# App static files
STATIC_URL = '/static/'
# Production static files
STATIC_ROOT = os.path.join(BASE_DIR, 'root')
# Project static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Media storage settings

# URL to use in templates for the files
MEDIA_URL = '/media/'
# absolute filesystem path to the directory for user-uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTHENTICATION_BACKENDS = [
 "django.contrib.auth.backends.ModelBackend",
 "allauth.account.auth_backends.AuthenticationBackend",
]


# Abstract user model
AUTH_USER_MODEL = 'users.User'

# django-allauth settings

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_REDIRECT_URL = 'pages:home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'pages:home'

# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# change to login page
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'pages:home'


# development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# production
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.community.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'community@hub.com'
EMAIL_HOST_PASSWORD = 'password'
SERVER_EMAIL = 'community@hub.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

REGISTERED_COMMUNITIES = [
    ('JSY', 'Jersey'),
    ('GSY', 'Guernsey'),
    ('ADY', 'Alderny'),
    ('SARK', 'Sark'),
    ('HERM', 'Herm')
]