from celery import shared_task
from .notifications.email import send_email
from .notifications.sms import send_sms
from .notifications.whatsapp import send_whatsapp

@shared_task(bind=True)
def send_email_task(self, email_user, email_pass, email_host, email_port, subject, message, to):
    config = {
        "EMAIL_HOST_USER": email_user,
        "EMAIL_HOST_PASSWORD": email_pass,
        "EMAIL_HOST": email_host,
        "EMAIL_PORT": email_port
    }
    return send_email(config, subject, message, to)

@shared_task(bind=True)
def send_sms_task(self, sid, token, from_, msg, to):
    config = {
        "TWILIO_ACCOUNT_SID": sid,
        "TWILIO_AUTH_TOKEN": token,
        "TWILIO_PHONE_NUMBER": from_
    }
    return send_sms(config, msg, to)

@shared_task(bind=True)
def send_whatsapp_task(self, sid, token, from_, msg, to):
    config = {
        "TWILIO_ACCOUNT_SID": sid,
        "TWILIO_AUTH_TOKEN": token,
        "TWILIO_WHATSAPP_NUMBER": from_
    }
    return send_whatsapp(config, msg, to)