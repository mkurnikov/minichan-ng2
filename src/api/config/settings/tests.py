from .common import *
from .application import *


DEBUG = False
ALLOWED_HOSTS = tenv.getlist('DJANGO_ALLOWED_HOSTS', default=['*']) + \
                ['localhost', '127.0.0.1']  # Ensures we can run DEBUG = False locally

SECRET_KEY = tenv.get("DJANGO_SECRET_KEY",
                      default='h@z@&1zuwxd%dy#%2o(vfivq7r^+8pu0y4re4ua1=!25=$kd@#')