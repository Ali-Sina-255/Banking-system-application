from os import getenv, path

from dotenv import load_dotenv

from .base import  *

from .base import  BASE_DIR

local_ven_file = path.join(BASE_DIR,'.vens','.ven.local')

if path.isfile(local_ven_file):
    load_dotenv(local_ven_file)

DEBUG = True
SITE_NAME = getenv("SITE_NAME")
SECRET_KEY =getenv("DJANGO_SECRET_KEY","y0lfREmNZTq5Ll-b5Cv-oSKkU_cfYbQTgD9hybBYcHMfiZGWa5E")
# "django-insecure-1!fxsryp$_kcc617+(@bbm9)0u3&p1a20y@vvbm1#l)(cykpck"

# generated secret_kes
# python -c "import secrets; print(secrets.token_urlsafe(38))"
ALLOWED_HOSTS = ["localhost","0.0.0.0","127.0.0.1"]

DJANGO_ADMIN_URL = getenv("DJANGO_ADMIN_URL")
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
DOMAIN = getenv("DOMAIN")