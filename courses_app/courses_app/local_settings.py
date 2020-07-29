import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'courses_app',
        'USER': 'naku',
        'PASSWORD': 'naku',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

DEBUG = True