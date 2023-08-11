"""
Django settings for picoprobe_portal project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import logging
from pathlib import Path

log = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "insecure-local-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # TODO: What else to add here? rpl_portal info adapted below.
    "globus_portal_framework",
    "picoprobe_portal",
    "social_django",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # TODO: What else to add here? rpl_portal info adapted below.
    "globus_portal_framework.middleware.ExpiredTokenMiddleware",
    "globus_portal_framework.middleware.GlobusAuthExceptionMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

# TODO: Add AUTHENTICATION_BACKENDS? rpl_portal has it (copied below).
AUTHENTICATION_BACKENDS = [
    "globus_portal_framework.auth.GlobusOpenIdConnect",
    "django.contrib.auth.backends.ModelBackend",
]

ROOT_URLCONF = "testing.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # TODO: Populate templates directory
        "DIRS": [BASE_DIR / "picoprobe_portal" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # TODO: What else to add here? rpl_portal info adapted below.
                "globus_portal_framework.context_processors.globals",
            ],
        },
    },
]

# TODO: Add LOGGING? rpl_portal has it (copied below).
LOGGING = {
    "version": 1,
    "handlers": {
        "stream": {"level": "DEBUG", "class": "logging.StreamHandler"},
    },
    "loggers": {
        "django": {"handlers": ["stream"], "level": "INFO"},
        "globus_portal_framework": {"handlers": ["stream"], "level": "INFO"},
        "picoprobe_portal": {"handlers": ["stream"], "level": "INFO"},
    },
}

WSGI_APPLICATION = "testing.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# TODO: rpl_portal does not have AUTH_PASSWORD_VALIDATORS, do we need it?
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

# TODO: rpl_portal does not have USE_L10N (copied below), do we need it?
# USE_L10N = True

USE_TZ = True


# TODO: rpl_portal has "/static/", do we need to change the below?
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# TODO: Do we need this? rpl_portal has it (copied below).
try:
    from .local_settings import *
except ImportError:
    expected_path = Path(__file__).resolve().parent / "local_settings.py"
    log.warning(f"You should create a file for your secrets at {expected_path}")