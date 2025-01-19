from os import getenv, path

from dotenv import load_dotenv
from .base import  *

from .base import  BASE_DIR

local_ven_file = path.join(BASE_DIR,'.vens','.ven.local')

if path.isfile(local_ven_file):
    load_dotenv(local_ven_file)

SECRET_KEY =getenv("DJANGO_SECRET_KEY")


# generated secret_kes
# python -c "import secrets; print(secrets.token_urlsafe(38))"
# change in the production
ALLOWED_HOSTS = ["localhost","0.0.0.0","127.0.0.1"]

DJANGO_ADMIN_URL = getenv("DJANGO_ADMIN_URL")

DOMAIN = [
    ("Ali Sina Sultani",'alisinasultani255@gmail.com')
]