import os
import random
import string

SECRET_KEY = [random.choice(string.ascii_lowercase) for i in range(10)]

DATABASES = {
    'default':
        {
            'ENGINE': 'iseries',
            'NAME': 'iseries',  # arbitrary database name for db2 on iseries
            'HOST': 'pub400.com',
            'USER': os.environ['TEST_SYSTEM_USERNAME'],
            'PASSWORD': os.environ['TEST_SYSTEM_PASSWORD'],
            'CURRENTSCHEMA': os.environ['TEST_SYSTEM_SCHEMA'],
        }
}

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.staticfiles',

    'tests',
]