from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv('DB_NAME'),
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "HOST": os.getenv('DB_HOST'),
        "PORT": os.getenv('DB_PORT'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
]

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static', f'v{STATIC_VERSION}')

STATIC_URL = f'/static/v{STATIC_VERSION}/'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
