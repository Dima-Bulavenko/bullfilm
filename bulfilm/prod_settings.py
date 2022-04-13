import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4@t__a0sg(0=7eg*bzl-7u!j)-!&@*wsg#3n@*ds_s_0_b#^ty'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '164.92.242.174',]

# Application definition


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bullfilm',
        'USER': 'dima',
        'PASSWORD': 'gavgavgav',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SASS_PROCESSOR_ROOT = STATIC_ROOT
