from rest_framework.decorators import api_view
from rest_framework.response import Response
from .notifications.dispatcher import handle_notification

@api_view(["POST"])
def notify_user(request):
    method = request.data.get("method")
    to = request.data.get("to")
    message = request.data.get("message")
    subject = request.data.get("subject", "")  # optional

    if method == "email":
        send_email_task.delay(subject, message, to)
    elif method == "sms":
        send_sms_task.delay(message, to)
    elif method == "whatsapp":
        send_whatsapp_task.delay(message, to)
    else:
        return Response({"error": "Invalid method"}, status=400)

    return Response({"status": "Notification task triggered!"})
