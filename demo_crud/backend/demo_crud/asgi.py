"""
ASGI config for demo_crud project.

It exposes the ASGI callable as a module-level variable named ``application``.

This is used for async servers like Daphne or Uvicorn.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo_crud.settings")

application = get_asgi_application()
