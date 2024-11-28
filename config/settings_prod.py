from __future__ import annotations

import os

import dj_database_url
import environ

from .settings import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

DATABASES = {'default': dj_database_url.config(conn_health_checks=True)}
