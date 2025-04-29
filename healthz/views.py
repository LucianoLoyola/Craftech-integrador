from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
import logging

logger = logging.getLogger(__name__)

@api_view(["GET"])
def index(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 + 1")
            rows = cursor.fetchall()
        return Response()
    except Exception as e:
        logger.exception(e)
        return Response(status=500)