# coding: utf-8
from __future__ import unicode_literals


"""Common settings and globals."""


from os.path import abspath, basename, dirname, join, normpath
from sys import path


# PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
# END PATH CONFIGURATION


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION


# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (  
    ('Sean Chamberlain', 'sean@pixeltotheleft.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',    # use dj-database-url instead
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Heroku uses this to configure DB access.
import dj_database_url

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# END DATABASE CONFIGURATION


# GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Australia/Adelaide'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = False    # slight performance boost

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# END GENERAL CONFIGURATION


# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = ()

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# DEFAULT_FILE_STORAGE = 'skinnee.settings.s3utils.MediaRootS3BotoStorage'

# AWS_ACCESS_KEY_ID = 'AKIAJH4L6WYB5MIXGJ7A'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'tulare-skinnee'
# AWS_PRELOAD_METADATA = True

# STATICFILES_STORAGE = 'skinnee.settings.s3utils.StaticRootS3BotoStorage'

STATIC_URL = '/static/'
# # END STATIC FILE CONFIGURATION


# Disable in-memory uploads. Slight performance hit, but trade-off probably
# worth it - far simpler
FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",)


# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
# MEDIA_URL = 'http://tulare-skinnee.s3-website-us-west-1.amazonaws.com/django-media/'
# END MEDIA CONFIGURATION


# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"74z+!vm*8fb5rq+ospp2r$slxg9*pcz@rs$af%v^0ara452!342"
# END SECRET CONFIGURATION


# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost']
# END SITE CONFIGURATION


# FIXTURE CONFIGURATION
# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
# END FIXTURE CONFIGURATION


# TEMPLATE CONFIGURATION
# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
# END TEMPLATE CONFIGURATION


# MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)
# END MIDDLEWARE CONFIGURATION


# URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
# END URL CONFIGURATION


# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',
    # Django management
    'django_extensions',
#     # APIs
    'rest_framework',
#     'rest_framework.authtoken',
    'rest_framework_swagger',   # REST API autodoc
#     'spyne',                    # SOAP API
#     # Auth
#     'provider',
#     'provider.oauth2',
#     # Form handling
#     'floppyforms',
#     'crispy_forms',
#     'djangular',
#     # User
#     'userena',
#     'guardian',
#     'easy_thumbnails',
#     'userena.contrib.umessages',
#     # Model Versioning
#     'reversion',
#     # CORS
#     'corsheaders',
#     # Static file upload to S3
#     'storages',
#     # Text search without monthly fee
#     #'watson',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'league',
    'player',
    'core'
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS 
# END APP CONFIGURATION


# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# END LOGGING CONFIGURATION


# WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
# END WSGI CONFIGURATION


# REST CONFIGURATION
# REST_FRAMEWORK = {
#     'PAGINATE_BY': 5,
#     'PAGINATE_BY_PARAM': 'page_size',
#     'DEFAULT_FILTER_BACKENDS': (
#         'rest_framework.filters.DjangoFilterBackend',
#         'rest_framework.filters.SearchFilter',
#         'rest_framework.filters.OrderingFilter'),

#     # Use hyperlinked styles by default.
#     # Only used if the `serializer_class` attribute is not set on a view.
#     'DEFAULT_MODEL_SERIALIZER_CLASS':
#     'rest_framework.serializers.HyperlinkedModelSerializer',

#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.

#     # TODO no unauthenticated access, even read-only
#     'DEFAULT_PERMISSION_CLASSES': [
#         #'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.AllowAny',  # TESTING ONLY
#     ],

#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         #'rest_framework.authentication.OAuth2Authentication',
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     )
# }
# END REST CONFIGURATION

# SWAGGER CONFIGURATION
# SWAGGER_SETTINGS = {
#     "exclude_namespaces": [],  # List URL namespaces to ignore
#     "api_version": 'v0',  # Specify your API's version
#     "enabled_methods": [  # Specify which methods to enable in Swagger UI
#         'get',
#         'post',
#         'put',
#         'patch',
#         'delete'
#     ],
#     "api_key": '',  # An API key
# }
# END SWAGGER CONFIGURATION


# # Various stupidity needed to get Django and AngularJS to play nice.
# CORS_ORIGIN_ALLOW_ALL = True
# APPEND_SLASH = False        # http://stackoverflow.com/a/17476462/1859001

