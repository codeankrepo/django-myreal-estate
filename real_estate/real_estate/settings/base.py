from pathlib import Path

import environ

from decouple import config

SECRET_KEY = config("SECRET_KEY")

env = environ.Env(DEBUG = (bool, False)) # here we are storing our env variable

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# an expression to read environment varibles given in base directory

environ.Env.read_env(BASE_DIR / ".env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-nx=rr%fq)y1+_kk+_jopt9hl^gu4-hvubw8v)=rjrpsky00d6$'

# SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# DEBUG = env("DEBUG")

DEBUG = config("DEBUG")

# ALLOWED_HOSTS = []

# ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")
ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(" ") 
'''
 this split will provide a list of value which will be separated by spaces
 for example ALLOWED_HOSTS = "example.com localhost 127.0.0.1"
 ALLOWED_HOSTS = ["example.com", "localhost", "127.0.0.1"]


'''

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # third-party apps are mentioned here <- <- <- <-
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    # "djoser",
    # "rest_framework_simplejwt",
    # "djcelery_email", 

    # my apps <- <- <- <-
    "apps.common",
    "apps.users",
    "apps.profiles",
    "apps.ratings",
    # "apps.properties",
    # "apps.enquiries",
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real_estate.urls'

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

WSGI_APPLICATION = 'real_estate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIR = []

MEDIA_URL = '/mediafiles'
MEDIA_ROOT = BASE_DIR / 'mediafiles'
MEDIAFILES_DIR = []

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
