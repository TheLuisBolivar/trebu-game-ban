import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'trebu_game_ban',
        'HOST': 'trebu-game-ban.cbaua8ucfsda.us-east-2.rds.amazonaws.com',
        'USER': 'trebu_user',
        'PASSWORD': 'Tr3Bu!-2023_G4m3-B4nn',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
