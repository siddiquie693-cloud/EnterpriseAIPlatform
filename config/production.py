from .settings import *

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = BASE_DIR / "media"

CSRF_TRUSTED_ORIGINS = []