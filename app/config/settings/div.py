import os
import environ

from .base import *
from .internationalization import *


INSTALLED_APPS +=[
    'rosetta',
    'debug_toolbar',
    


    'django_cleanup.apps.CleanupConfig',  #must be the last app  https://github.com/un1t/django-cleanup
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


SECRET_KEY = 'django-insecure-4)s!+l(hry#!=oyltl=_g#8_$8%2vuf7_)%vv)49(le-k3=n22'
DEBUG = True
ALLOWED_HOSTS = []
ADMIN_URL= 'admin/'

env = environ.Env()
#ENV_BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


env.read_env(os.path.join(BASE_DIR, 'envvar', 'dev','.postgres'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
        'ATOMIC_REQUESTS':True,
        'CONN_MAX_AGE':60,
    }
}




MEDIA_ROOT= os.path.join(BASE_DIR, 'media')

env.read_env(os.path.join(BASE_DIR, 'envvar', 'dev','.rabbitmq'))

CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = f'amqp://{env.str('RABBITMQ_DEFAULT_USER')}:{env.str('RABBITMQ_DEFAULT_PASS')}@localhost:5672//'





# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        # Disable profiling panel due to an issue with Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'db_log': {
            'level': 'DEBUG',
            'class': 'db_logger.db_log_handler.DatabaseLogHandler'
        },
    },
    'loggers': {
        'db': {
            'handlers': ['db_log'],
            'level': 'DEBUG'
        },
        'django.request': { # logging 500 errors to database
            'handlers': ['db_log'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}