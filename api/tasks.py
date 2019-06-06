from datetime import timedelta, datetime

import sendgrid
from celery import shared_task
from django.template.loader import get_template
from sendgrid.helpers.mail import *

from api.models import User, Workspace, Site
from tukole.settings import SENDGRID_API_KEY, SERVER_URL


@shared_task
def send_invite_email(receiver_user_id, token, sender_user_id, workspace):
    sender = User.objects.filter(id=sender_user_id).first()
    receiver = User.objects.filter(id=receiver_user_id).first()
    workspace = Workspace.objects.filter(id=workspace).first()
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(email="no-reply@tukole.co.ug", name="Tukole System")
    to_email = Email(receiver.email)
    subject = "Tukole Workspace invite"
    sender_name = ""
    if sender:
        if sender.first_name and sender.last_name:
            sender_name = "%s %s" % (sender.first_name, sender.last_name)
    else:
        sender_name = "A Tukole Admin"

    ctx = {
        "receiver_name": "%s %s" % (receiver.first_name, receiver.last_name),
        "sender_name": "%s" % sender_name,
        "accept_link": "%s/%s/%s/" % (SERVER_URL, "users/accept", token),
        "server_url": SERVER_URL,
        "workspace": workspace.name.lower()
    }
    content = Content("text/html", get_template('email/invite_users.html').render(context=ctx))
    # message = get_template('email/meeting_confirmation.html').render(context=ctx)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


@shared_task
def send_challenge_email(receiver_user_id, sender_user_id, challenge_id):
    sender = User.objects.filter(id=sender_user_id).first()
    receiver = User.objects.filter(id=receiver_user_id).first()
    from api.models import Challenge
    challenge = Challenge.objects.filter(id=challenge_id).first()
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(email="no-reply@tukole.co.ug", name="Tukole System")
    to_email = Email(receiver.email)
    subject = "Tukole Workspace Challenge"
    sender_name = ""
    if sender:
        if sender.first_name and sender.last_name:
            sender_name = "%s %s" % (sender.first_name, sender.last_name)
    else:
        sender_name = "A Tukole Admin"

    ctx = {
        "receiver_name": "%s %s" % (receiver.first_name, receiver.last_name),
        "sender_name": "%s" % sender_name,
        "challenge_title": challenge.title,
        "challenge_site": challenge.site.site_name,
        "challenge_description": challenge.description,
        "server_url": SERVER_URL,
        "challenge_type": challenge.type
    }
    content = Content("text/html", get_template('email/site_challenge.html').render(context=ctx))
    # message = get_template('email/meeting_confirmation.html').render(context=ctx)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


@shared_task
def send_trip_cancel_email(receiver_user_id, sender_user_id, trip_id):
    sender = User.objects.filter(id=sender_user_id).first()
    receiver = User.objects.filter(id=receiver_user_id).first()
    from api.models import Trip
    trip = Trip.objects.filter(id=trip_id).first()
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(email="no-reply@tukole.co.ug", name="Tukole System")
    to_email = Email(receiver.email)
    subject = "Tukole Workspace Challenge"
    sender_name = ""
    if sender:
        if sender.first_name and sender.last_name:
            sender_name = "%s %s" % (sender.first_name, sender.last_name)
    else:
        sender_name = "A Tukole Admin"

    ctx = {
        "receiver_name": "%s %s" % (receiver.first_name, receiver.last_name),
        "sender_name": "%s" % sender_name,
        "trip_reason": trip.reason_for_cancellation,
        "trip_site": trip.site.site_name,
        "server_url": SERVER_URL,
    }
    content = Content("text/html", get_template('email/user_cancelled_trip.html').render(context=ctx))
    # message = get_template('email/meeting_confirmation.html').render(context=ctx)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


@shared_task
def send_reset_password_email(receiver_user_id, token):
    receiver = User.objects.filter(id=receiver_user_id).first()
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(email="no-reply@tukole.co.ug", name="Tukole System")
    to_email = Email(receiver.email)
    subject = "Tukole Workspace Password Reset"
    ctx = {
        "receiver_name": "%s %s" % (receiver.first_name, receiver.last_name),
        "accept_link": "%s/%s/%s/" % (SERVER_URL, "users/accept", token),
        "server_url": SERVER_URL,
    }
    content = Content("text/html", get_template('email/reset_password.html').render(context=ctx))
    # message = get_template('email/meeting_confirmation.html').render(context=ctx)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


@shared_task()
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


@shared_task()
def get_survey_due_in_3days():
    now = datetime.now()
    in_3_days = now + timedelta(days=3)
    sites_to_be_reminded = Site.objects.filter(survey_date__range=[now, in_3_days], email_remainder_sent=False)
    for site in sites_to_be_reminded:
        receivers = [site.clientId.id, site.surveyor.id]
        send_survey_reminder_email.delay(receivers=receivers, site_id=site.id)
