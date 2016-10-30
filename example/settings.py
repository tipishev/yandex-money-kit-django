# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import sys
import os.path

try:
    from settings_local import *
except ImportError:
    print("Don't forget create settings_local.py")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, '..'))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'SECRET_KEY'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'example/templates')],
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

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'app',
    'yandex_money',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

YANDEX_MONEY_SCID = 123
YANDEX_MONEY_SHOP_ID = 456
YANDEX_MONEY_SHOP_PASSWORD = 'password'
YANDEX_MONEY_DEBUG = DEBUG
YANDEX_MONEY_FAIL_URL = 'http://example.com/fail-payment/'
YANDEX_MONEY_SUCCESS_URL = 'http://example.com/success-payment/'

try:
    from settings_local import *
except ImportError:
    pass
