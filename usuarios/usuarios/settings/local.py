from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3', se modifico esta lines AVH
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME' : get_secret('DB_NAME'),
        'USER' : get_secret('USER'),
        'PASSWORD' : get_secret('PASSWORD'),
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Configuracion para archivos estaticos
STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]

#Configuracion para archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')