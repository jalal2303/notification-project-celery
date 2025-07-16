import os
from celery import shared_task
from .notifications.email import send_email
from .notifications.sms import send_sms
from .notifications.whatsapp import send_whatsapp

@shared_task
def send_email_task(subject, message, to):
    config = {
        "EMAIL_HOST_USER": os.getenv("EMAIL_HOST_USER"),
        "EMAIL_HOST_PASSWORD": os.getenv("EMAIL_HOST_PASSWORD"),
        "EMAIL_HOST": os.getenv("EMAIL_HOST"),
        "EMAIL_PORT": os.getenv("EMAIL_PORT")
    }
    return send_email(config, subject, message, to)

@shared_task
def send_sms_task(message, to):
    config = {
        "TWILIO_ACCOUNT_SID": os.getenv("TWILIO_ACCOUNT_SID"),
        "TWILIO_AUTH_TOKEN": os.getenv("TWILIO_AUTH_TOKEN"),
        "TWILIO_PHONE_NUMBER": os.getenv("TWILIO_PHONE_NUMBER")
    }
    return send_sms(config, message, to)

@shared_task
def send_whatsapp_task(message, to):
    config = {
        "TWILIO_ACCOUNT_SID": os.getenv("TWILIO_ACCOUNT_SID"),
        "TWILIO_AUTH_TOKEN": os.getenv("TWILIO_AUTH_TOKEN"),
        "TWILIO_WHATSAPP_NUMBER": os.getenv("TWILIO_WHATSAPP_NUMBER")
    }
    return send_whatsapp(config, message, to)
