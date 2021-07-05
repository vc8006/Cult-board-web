import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n)*j7j&5g!a%tb9m8m(17n)_***7j9ora+*s-zh+n5$%^bwv@i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'microsoft_authentication',
    'lumiere.apps.LumiereConfig',
    # 'authentication',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.microsoft',
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

ROOT_URLCONF = 'cult_board.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'microsoft_auth.context_processors.microsoft',
            ],
        },
    },
]

WSGI_APPLICATION = 'cult_board.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# AUTHENTICATION_BACKENDS = [
#     'microsoft_auth.backends.MicrosoftAuthenticationBackend',
#     'django.contrib.auth.backends.ModelBackend' # if you also want to use Django's authentication
#     # I recommend keeping this with at least one database superuser in case of unable to use others
# ]

# # values you got from step 2 from your Mirosoft app
# MICROSOFT_AUTH_CLIENT_ID = 'db37acd0-8776-44d1-adc8-b257495f63b8'
# MICROSOFT_AUTH_CLIENT_SECRET = '2cb8e0c9-a6ea-4709-a9c2-68ba46a05aa4'
# # Tenant ID is also needed for single tenant applications
# # MICROSOFT_AUTH_TENANT_ID = 'your-tenant-id-from-apps.dev.microsoft.com'

# # pick one MICROSOFT_AUTH_LOGIN_TYPE value
# # Microsoft authentication
# # include Microsoft Accounts, Office 365 Enterpirse and Azure AD accounts
# MICROSOFT_AUTH_LOGIN_TYPE = 'ma'

# MICROSOFT = {
#     "app_id": "db37acd0-8776-44d1-adc8-b257495f63b8",
#     "app_secret": "U0.K6H8CoGXo-xKs-c_R69jf~j93A9dI2v",
#     "redirect": "http://localhost:8000/microsoft_authentication/callback",
#     "scopes": ["user.read"],
#     "authority": "https://login.microsoftonline.com/common",  # or using tenant "https://login.microsoftonline.com/{tenant}",
#     "valid_email_domains": ["<list_of_valid_domains>"],
#     "logout_uri": "http://localhost:8000/admin/logout"
# }

# LOGIN_URL = "/microsoft_authentication/login"
LOGIN_REDIRECT_URL = "/"  # optional and can be changed to any other url

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'microsoft': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'db37acd0-8776-44d1-adc8-b257495f63b8',
            'secret': 'U0.K6H8CoGXo-xKs-c_R69jf~j93A9dI2v',
            'key': ''
        }
    }
}