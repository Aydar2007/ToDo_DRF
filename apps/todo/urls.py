from django.urls import path
from apps.todo.views import ToDoAPIViewSet, ToDoAllDelete
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todo', ToDoAPIViewSet, 'api_todo')
urlpatterns = [
    path('todo_all_delete', ToDoAllDelete.as_view(), name="todo_all_delete")
]
urlpatterns += router.urls 