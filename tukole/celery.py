from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tukole.settings')

app = Celery('tukole')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_survey_reminder_email_every_day': {
        'task': 'api.tasks.get_survey_due_in_3days',
        'schedule': crontab(minute=0, hour=1)
    },
}
