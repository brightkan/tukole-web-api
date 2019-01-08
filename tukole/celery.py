from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
from tukole.settings import SENDGRID_API_KEY, SERVER_URL
import sendgrid
from sendgrid.helpers.mail import *
from django.template.loader import get_template
from datetime import timedelta, datetime

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tukole.settings')

app = Celery('tukole')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task
def send_survey_reminder_email():
    from api.models import User, Workspace, Site
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    startdate = datetime.now()
    enddate = startdate + timedelta(days=3)
    sites_to_be_reminded = Site.objects.filter(survey_date__range=[startdate, enddate])
    for site in sites_to_be_reminded:
        print("alsjd;alsdljasl;djas das;ldjas;ldj;lasjd sa;ldjsljasl;d")
        from_email = Email(email="no-reply@tukole.co.ug", name="Tukole System")
        to_emails = [site.clientId, site.surveyor]
        subject = "Tukole Survey Remainder"

        client_email = site.clientId.email
        surveyor = site.surveyor.email

        ctx = {
            "client_name": "%s %s" % (site.clientId.first_name, site.clientId.last_name),
            "site_name": "%s" % (site.site_name),
            "survey_date": site.survey_date,
            "survey_time": site.survay_time,
        }

        for receiver in to_emails:
            ctx['receiver_name'] = "%s %s" % (receiver.first_name, receiver.last_name)
            content = Content("text/html", get_template('email/survey_remainder.html').render(context=ctx))
            mail = Mail(from_email, subject, Email(receiver.email), content)
            response = sg.client.mail.send.post(request_body=mail.get())



app.conf.beat_schedule = {
    # Executes every day at 8:00 a.m.
    'add-every-monday-morning': {
        'task': 'tukole.celery.send_survey_reminder_email',
        'schedule': crontab(minute=0, hour=8)
    },
}