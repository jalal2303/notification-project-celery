from rest_framework.decorators import api_view
from rest_framework.response import Response
from .notifications.dispatcher import handle_notification

@api_view(["POST"])
def send_notification(request, project):
    result = handle_notification(project, request.data)
    return Response({"project": project, "status": "done", "details": result})