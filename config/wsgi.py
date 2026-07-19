"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Run database migrations at startup
import django
django.setup()
from django.core.management import call_command
try:
    print("Startup: Running database migrations...")
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Failed to run database migrations at startup: {e}")

application = get_wsgi_application()
app = application

