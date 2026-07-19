"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

class TracebackApp:
    def __init__(self, tb_text):
        self.tb_text = tb_text

    def __call__(self, environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        return [f"DJANGO INITIALIZATION ERROR ON VERCEL\n\n{self.tb_text}".encode('utf-8')]

try:
    import django
    django.setup()
    from django.core.management import call_command
    try:
        print("Startup: Running database migrations...")
        call_command('migrate', interactive=False)
    except Exception as e:
        print(f"Failed to run database migrations at startup: {e}")

    from django.core.wsgi import get_wsgi_application
    raw_application = get_wsgi_application()
    
    def application(environ, start_response):
        try:
            return raw_application(environ, start_response)
        except Exception as e:
            tb = traceback.format_exc()
            status = '500 Internal Server Error'
            headers = [('Content-Type', 'text/plain; charset=utf-8')]
            start_response(status, headers)
            return [f"DJANGO REQUEST RUNTIME ERROR\n\n{tb}".encode('utf-8')]

except Exception as e:
    tb_text = traceback.format_exc()
    application = TracebackApp(tb_text)

app = application

