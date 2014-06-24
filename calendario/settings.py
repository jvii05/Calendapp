"""
Django settings for calendario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2);

# Parse database configuration from $DATABASE_URL
import dj_database_url
import os

#DATABASES['default'] =  dj_database_url.config('postgres://vkaymtljscsmgs:IleTvvOjyqlNQyVTOsGndmnkRI@ec2-50-17-207-54.compute-1.amazonaws.com:5432/d76i92n2getef3')
DATABASES = {'default':dj_database_url.config(default='postgres://vkaymtljscsmgs:IleTvvOjyqlNQyVTOsGndmnkRI@ec2-50-17-207-54.compute-1.amazonaws.com:5432/d76i92n2getef3')}


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
 
 
# Allow all host headers
ALLOWED_HOSTS = ['*']
 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/ 
# Static asset configuration
#STATIC_ROOT = 'staticfiles'
STATIC_ROOT = ''
STATIC_URL = '/static/'
#LOGIN_REDIRECT_URL = '/' 
 
STATICFILES_DIRS = (
	RUTA_PROYECTO.child('static'),
    #os.path.join(BASE_DIR, 'static'),
)

#STATICFILES_FINDERS = (
#	'django.contrib.staticfiles.finders.FileSystemFinder',
#	'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
#)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(y$zli)x_zp#lu6q(j!q$+0dnslvp&3n6+#$fi9bjjyl04b^t$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
	RUTA_PROYECTO.child('templates'),
)

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social.apps.django_app.default',
    'apps.inicio',
    'apps.usuario',
    'apps.procesos',
    'apps.entidades',
    'apps.logueo',
    'django_extensions',
)

TEMPLATE_CONTEXT_PROCESORS = (
	'django.contrib.auth.context_processors-auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.il8n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
	'django.contrib.messages.context_processors.message',
	'social.apps.django_app.context_processors.backends',
	'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'calendario.urls'

WSGI_APPLICATION = 'calendario.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd76i92n2getef3',
        'HOST': 'ec2-50-17-207-54.compute-1.amazonaws.com',
        'USER': 'vkaymtljscsmgs', 
		'PORT': '5432',
		'PASSWORD': 'IleTvvOjyqlNQyVTOsGndmnkRI',
    }
}

SOCIAL_AUTH_FACEBOOK_KEY = '1404657089754838'
SOCIAL_AUTH_FACEBOOK_SECRET = '73b5603c0c2d89d223ba08c8b4ba6fb7'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_SCOPE = 'email,publish_stream'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-cr'

#soluciona problema de conexion a bd: ImproperlyConfigured at /admin/
SITE_ID = 1


TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

