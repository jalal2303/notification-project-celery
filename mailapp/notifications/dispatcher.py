from mailapp.tasks import send_email_task, send_sms_task, send_whatsapp_task
from dotenv import dotenv_values
import os

def load_env(project):
    env_path = os.path.join("resources", f"env_{project}")
    return dotenv_values(env_path) if os.path.exists(env_path) else {}

def handle_notification(project, payload):
    config = load_env(project)
    if not config:
        return [f"❌ Config not found for: {project}"]

    subject = payload.get("subject", "Notification")
    body = payload.get("message_body")
    recipients = payload.get("recipients", [])

    responses = []
    for r in recipients:
        name = r.get("name", "User")
        email = r.get("email")
        phone = r.get("phone")
        message = f"Hi {name},\n\n{body}"

        if config.get("EMAIL_HOST_USER") and email:
            send_email_task.delay(
                config.get("EMAIL_HOST_USER"),
                config.get("EMAIL_HOST_PASSWORD"),
                config.get("EMAIL_HOST"),
                config.get("EMAIL_PORT", 587),
                subject, message, email
            )
            responses.append(f"📧 Email sent to {email}")

        if config.get("TWILIO_PHONE_NUMBER") and phone:
            send_sms_task.delay(
                config["TWILIO_ACCOUNT_SID"],
                config["TWILIO_AUTH_TOKEN"],
                config["TWILIO_PHONE_NUMBER"],
                message, phone
            )
            responses.append(f"📱 SMS sent to {phone}")

        if config.get("TWILIO_WHATSAPP_NUMBER") and phone:
            send_whatsapp_task.delay(
                config["TWILIO_ACCOUNT_SID"],
                config["TWILIO_AUTH_TOKEN"],
                config["TWILIO_WHATSAPP_NUMBER"],
                message, phone
            )
            responses.append(f"💬 WhatsApp sent to {phone}")

    return responses or ["⚠️ No valid channels available"]