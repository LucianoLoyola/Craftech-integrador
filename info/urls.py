from django.urls import path, include
from rest_framework import routers
from info.views import index

urlpatterns = [
    path("", index)
]