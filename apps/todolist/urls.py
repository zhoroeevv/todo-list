from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.todolist.views import ToDoViewSet

router = DefaultRouter()
router.register('todo', ToDoViewSet, basename='api_todo')

urlpatterns = router.urls
