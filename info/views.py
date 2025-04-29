from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging
import os

logger = logging.getLogger(__name__)

@api_view(["GET"])
def index(request):
    return Response(os.environ)