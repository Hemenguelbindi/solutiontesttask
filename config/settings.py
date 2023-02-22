from pathlib import Path
from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent

# Init environment variables for this and read
env = Env()
env.read_env()

SECRET_KEY = env.str('TOKEN_DJANGO_APP')

DEBUG = env('DEV')


ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "items",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

if env.bool("DEV"):
    DATABASES = {
    "default": {
        "ENGINE": env.str('DEV_DB'),
        "NAME": BASE_DIR / env.str('DEV_NAME'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': env.str('PROD_DB'),
            'NAME': env.str('NAME_DB'),
            'USER': env.str('PRODUCT_USER'),
            'Password': env.str('PRODUCT_PASSWORD'),
            'HOST': env.str('PRODUCT_HOST'),
            'PORT': env.str('PRODUCT_PORT'),
        }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STRUPE_PUBLIC_KEY = env.str('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = env.str('STRIPE_SECRET_KEY')
