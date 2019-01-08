from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta, datetime

import sendgrid
from celery import Celery
from celery.schedules import crontab
from django.template.loader import get_template
from sendgrid.helpers.mail import *

from api.models import Site, User
from tukole.settings import SENDGRID_API_KEY

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tukole.settings')

app = Celery('tukole')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def send_survey_reminder_email(receivers, site_id):
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(email="no-reply@tukole.co.ug", name="Tukole System")
    site = Site.objects.filter(id=site_id).first()
    if site:
        subject = "Tukole Survey Remainder"
        ctx = {
            "client_name": "%s %s" % (site.clientId.first_name, site.clientId.last_name),
            "site_name": "%s" % site.site_name,
            "survey_date": site.survey_date,
            "survey_time": site.survay_time,
        }

        for receiver_id in receivers:
            receiver = User.objects.filter(id=receiver_id).first()
            if receiver:
                ctx['receiver_name'] = "%s %s" % (receiver.first_name, receiver.last_name)
                content = Content("text/html", get_template('email/survey_remainder.html').render(context=ctx))
                mail = Mail(from_email, subject, Email(receiver.email), content)
                response = sg.client.mail.send.post(request_body=mail.get())
        site.email_remainder_sent = True
        site.save()
    else:
        pass


@app.task
def get_survey_due_in_3days():
    now = datetime.now()
    in_3_days = now + timedelta(days=3)
    sites_to_be_reminded = Site.objects.filter(survey_date__range=[now, in_3_days], email_remainder_sent=False)
    for site in sites_to_be_reminded:
        receivers = [site.clientId.id, site.surveyor.id]
        send_survey_reminder_email.delay(receivers=receivers, site_id=site.id)


app.conf.beat_schedule = {
    # Executes every day at 8:00 a.m.
    'send_survey_reminder_email_every_day': {
        'task': 'tukole.celery.get_survey_due_in_3days',
        'schedule': crontab(minute=0, hour=1)
    },
}
