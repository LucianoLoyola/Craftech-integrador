from django.urls import path, include
from rest_framework import routers
from healthz.views import index

urlpatterns = [
    path("", index)
]