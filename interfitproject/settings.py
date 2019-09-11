import os, json
from django.core.exceptions import ImproperlyConfigured
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECRET_KEY = os.environ['SECRET_KEY']



SECRET_KEY ="u(=gf%t)yleg@y!m^s5%5sabx6p+*g@f_)h0zt+n^=v&1o9mdp"

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','django-env.x2afusw42b.us-west-2.elasticbeanstalk.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'resumeapp.apps.ResumeappConfig',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'interfitproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['interfitproject/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'interfitproject.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': os.environ['DB_HOST'],
#         'PORT': os.environ['DB_PORT'],
#         'NAME': os.environ['DB_NAME'],
#         'USER': os.environ['DB_USER'],
#         'PASSWORD': os.environ['DB_PASSWORD'],
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
            "HOST": "interfitdbtest.cvkxhwqmhevj.us-east-2.rds.amazonaws.com" ,
            "PORT": "3306",
            "NAME": "interfitdbtest",
            "USER": "seung",
            "PASSWORD": "interfittest"  
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
