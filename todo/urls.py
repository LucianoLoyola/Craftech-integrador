from django.urls import path, include
from rest_framework import routers
from todo.views import ToDoViewSet

router = routers.DefaultRouter()
router.register('', ToDoViewSet)

urlpatterns = router.urls