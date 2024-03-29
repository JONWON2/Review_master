from pathlib import Path
import json
import os
from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")


DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '*', '127.0.0.1']

INSTALLED_APPS = [
    'board',
    'homeapp',
    'analysisapp',
    'accountapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'custom': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Busan1412',
        'USER': 'review_master',
        'PASSWORD':  get_secret("PASSWORD"),
        'HOST': get_secret("HOST"),
        'PORT': 1412
    }
}
DATABASE_ROUTERS = [
    'homeapp.router.DBRouter',
    'accountapp.router.DBRouter',
    'analysisapp.router.DBRouter',
    'board.router.DBRouter',
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_\
            validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_\
            validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_\
            validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_\
            validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'


STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 로그인 성공 시 자동으로 이동할 URL
LOGIN_REDIRECT_URL = '/home/home'
# 로그아웃 성공 시 자동으로 이동할 URL
LOGOUT_REDIRECT_URL = '/home/home'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 3600

# request 요청마다 session 정보를 저장하여 age값을 초기화, session 정보를 유지합니다.
# 해당 값이 false일 경우 쿠키 저장 시간이 만료되면 세션이 종료됩니다.
SESSION_SAVE_EVERY_REQUEST = True

# DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# 사용자가 업로드한 파일 관리
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
