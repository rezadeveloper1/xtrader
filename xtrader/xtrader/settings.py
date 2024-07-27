import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(int(os.environ.get('DEBUG', 1)))

ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)

LOGIN_REDIRECT_URL = "/accounts/%(username)s/"
LOGIN_URL = "/accounts/signin/"
LOGOUT_URL = "/accounts/signout/"
AUTH_PROFILE_MODULE = 'accounts.Profile'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140

USERENA_REDIRECT_ON_SIGNOUT = '/accounts/signin'
USERENA_SIGNIN_REDIRECT_URL = '/robots'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'accounts',
    'main',
    'django.contrib.sites',
    'finance',
    'data',
    'sales',
    'userena',
    'guardian',
    'easy_thumbnails',
    'social',
    'bootstrap3',
    'aum',
]

SITE_ID = 1
REDIS_DB = 0
INTERVALS = [1, 5, 10, 30, 60]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'xtrader.urls'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'xtrader.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'PORT': '5432',
    }
}

USE_TZ = True
TIME_ZONE = 'Iran'

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

USE_I18N = True
USE_L10N = True

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LOG_LEVEL = 'INFO'

try:
    from .localsetting import *
except ImportError:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}

ANONYMOUS_USER_NAME = "AnonymousUser"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'