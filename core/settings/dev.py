from .base import *

DEBUG = True
env.read_env()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


STATIC_URL = 'static/'
# MEDIA_URL='media/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')


