from .base import *
import environ

env = environ.Env()
environ.Env.read_env()
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
    }
}


STATIC_URL = 'static/'
# MEDIA_URL='media/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')


