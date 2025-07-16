web: gunicorn mailproject.wsgi:application
worker: celery -A mailproject worker --loglevel=info
