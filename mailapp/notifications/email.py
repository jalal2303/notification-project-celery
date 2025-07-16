import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(config, subject, message, to_email):
    msg = MIMEMultipart()
    msg["From"] = config["EMAIL_HOST_USER"]
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP(config["EMAIL_HOST"], int(config["EMAIL_PORT"]))
    server.starttls()
    server.login(config["EMAIL_HOST_USER"], config["EMAIL_HOST_PASSWORD"])
    server.send_message(msg)
    server.quit()
    return True