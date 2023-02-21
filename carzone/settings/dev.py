from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-5q4bs#@gpkqt%coi=t%-owjcp5q#z@kay!hb+fp%8aft_s_m_@'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'iman1376',
        'HOST': 'localhost',
    }
}


