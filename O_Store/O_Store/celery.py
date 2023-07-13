import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'O_Store.settings')
celery = Celery('O_Store')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()