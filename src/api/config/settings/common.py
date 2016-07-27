# -*- coding: utf-8 -*-
import logging.config

import os
from path import Path
from tenv import initialize_env


ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent  # up five levels
APPS_DIR = ROOT_DIR.joinpath('src/api/apps')

ENV_FILE = ROOT_DIR.joinpath('.env')
if os.path.isfile(ENV_FILE):
    tenv = initialize_env(ENV_FILE)
else:
    tenv = initialize_env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'src.api.apps.main',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'api_messaging.user_auth.middlewares.ResponseLoggingMiddleware'
)

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = tenv.getbool('DJANGO_DEBUG', default=True)

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': tenv.get('POSTGRESQL_DB_NAME'),
#         'USER': tenv.get('POSTGRESQL_USER'),
#         'PASSWORD': tenv.get('POSTGRESQL_PASSWORD'),
#         'HOST': tenv.get('POSTGRESQL_HOST'),
#         'PORT': tenv.get('POSTGRESQL_PORT'),
#     }
# }
# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'src.api.config.urls'

WSGI_APPLICATION = 'src.api.config.wsgi.application'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = APPS_DIR.joinpath('static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = ()

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING_CONFIG = None
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s] %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ROOT_DIR.joinpath('log/development.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'backupCount': 0,
            'formatter': 'verbose',
        },
        # 'swagger_logfile': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': ROOT_DIR.join('log/swagger_development.log').value,
        #     'maxBytes': 1024 * 1024 * 5,  # 5MB
        #     'backupCount': 0,
        #     'formatter': 'verbose',
        # },
    },
    'root': {
        'handlers': ['console', 'logfile'],
        'level': 'DEBUG',
    },
    'loggers': {
        # configure django loggers
        'django': {
            'level': 'INFO',
            'propagate': True,
        },
        # move all swagger-specific responses to the separate file
        # 'middlewares.swagger': {
        #     'level': 'INFO',
        #     'propagate': False,
        #     'handlers': ['swagger_logfile']
        # },
    }
})