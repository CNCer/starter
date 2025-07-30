import os

from .base import *
from .internationalization import *

DEBUG = False


INSTALLED_APPS +=[



    'django_cleanup.apps.CleanupConfig',  #must be the last app  https://github.com/un1t/django-cleanup
]

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
ADMIN_URL=  os.environ.get('DJANGO_ADMIN_URL')
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS',  '127.0.0.1').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS","https://127.0.0.1:8001").split(",")

#CSRF_TRUSTED_ORIGINS = ['http://<Raspberry_Pi_IP_Address>:8001', 'http://localhost:8001', 'http://127.0.0.1:8001']
#ALLOWED_HOSTS = ['<Raspberry_Pi_IP_Address>', 'localhost', '127.0.0.1']
#ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
        'ATOMIC_REQUESTS':True,
        'CONN_MAX_AGE':60,
    }
}

"""
# STATIC & MEDIA
# ------------------------
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
"""


# STATIC & MEDIA
# ------------------------
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}



MEDIA_ROOT= os.path.join(APP_DIR, 'media')
STATIC_ROOT = os.path.join(APP_DIR , 'staticfiles')


CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = f'amqp://{os.environ.get('RABBITMQ_DEFAULT_USER')}:{os.environ.get('RABBITMQ_DEFAULT_PASS')}@rabbitmq:5672//'

