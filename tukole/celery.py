from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta, datetime

import sendgrid
from celery import Celery
from celery.schedules import crontab
from django.template.loader import get_template
from sendgrid.helpers.mail import *

from tukole.settings import SENDGRID_API_KEY

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tukole.settings')

app = Celery('tukole')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def send_survey_reminder_email():
    from api.models import Site
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    startdate = datetime.now()
    enddate = startdate + timedelta(days=3)
    sites_to_be_reminded = Site.objects.filter(survey_date__range=[startdate, enddate], email_remainder_sent=False)
    for site in sites_to_be_reminded:
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
            site.email_remainder_sent = True
            site.save()


app.conf.beat_schedule = {
    # Executes every day at 8:00 a.m.
    'send_survey_reminder_email_every_day': {
        'task': 'tukole.celery.send_survey_reminder_email',
        'schedule': crontab(minute=0, hour=1)
    },
}
