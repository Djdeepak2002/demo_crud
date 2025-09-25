"""
WSGI config for demo_crud project.

It exposes the WSGI callable as a module-level variable named ``application``.

This is used by Gunicorn, uWSGI, etc.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo_crud.settings")




application = get_wsgi_application()
