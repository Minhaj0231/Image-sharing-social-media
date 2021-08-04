import os
from celery  import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_image.settings')

app = Celery('share_image')


app.config_from_object('django.conf:settings', namespace='CELERY' )

app.autodiscover_tasks()