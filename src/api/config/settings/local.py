from .common import *
from .application import *

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
DEBUG = True

SECRET_KEY = tenv.get("DJANGO_SECRET_KEY",
                      default='h@z@&1zuwxd%dy#%2o(vfivq7r^+8pu0y4re4ua1=!25=$kd@#')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
}