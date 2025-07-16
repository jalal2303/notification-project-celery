from twilio.rest import Client

def send_sms(config, message, phone):
    client = Client(config["TWILIO_ACCOUNT_SID"], config["TWILIO_AUTH_TOKEN"])
    client.messages.create(body=message, from_=config["TWILIO_PHONE_NUMBER"], to=phone)
    return True