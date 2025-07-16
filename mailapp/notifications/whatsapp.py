from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

def send_whatsapp(config, message, phone):
    try:
        client = Client(config["TWILIO_ACCOUNT_SID"], config["TWILIO_AUTH_TOKEN"])
        
        # FORMATTING RULES:
        # FROM: MUST be your Twilio sandbox number (format: whatsapp:+14155238886)
        # TO: MUST start with country code (format: whatsapp:+[countrycode][number])
        
        from_num = config["TWILIO_WHATSAPP_NUMBER"]
        to_num = phone
        
        # Force correct formatting
        if not from_num.startswith('whatsapp:'):
            from_num = f'whatsapp:{from_num}'
        if not to_num.startswith('whatsapp:'):
            to_num = f'whatsapp:{to_num}'
        
        # Remove all non-digit characters except '+' and 'whatsapp:'
        to_num = ''.join([c for c in to_num if c.isdigit() or c == '+'])
        to_num = f'whatsapp:{to_num}'  # Re-add prefix after cleaning
        
        # SANITY CHECK
        if not to_num.startswith('whatsapp:+'):
            raise ValueError(f"Invalid WhatsApp number format: {to_num}")
        
        message = client.messages.create(
            body=message,
            from_=from_num,  # e.g. "whatsapp:+14155238886"
            to=to_num        # e.g. "whatsapp:+919876543210"
        )
        return True
    except TwilioRestException as e:
        print(f"🚨 TWILIO ERROR: {e}")
        return False