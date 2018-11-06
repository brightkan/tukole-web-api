import sendgrid
from celery import shared_task
from django.template.loader import get_template
from sendgrid.helpers.mail import *

from api.models import User
from tukole.settings import SENDGRID_API_KEY, SERVER_URL


@shared_task
def send_invite_email(receiver_user_id, token, sender_user_id):
    sender = User.objects.filter(id=sender_user_id).first()
    receiver = User.objects.filter(id=receiver_user_id).first()
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email("no-reply@tukole.co.ug")
    to_email = Email(receiver.email)
    subject = "Tukole Workspace invite"
    ctx = {
        "receiver_name": "%s %s" % (receiver.first_name, receiver.last_name),
        "sender_name": "%s %s" % (sender.first_name, sender.last_name),
        "accept_link": "%s/%s/%s/" % (SERVER_URL, "users/accept", token),
        "server_url": SERVER_URL
    }
    content = Content("text/html", get_template('email/invite_users.html').render(context=ctx))
    # message = get_template('email/meeting_confirmation.html').render(context=ctx)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
