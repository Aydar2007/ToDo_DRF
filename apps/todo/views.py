from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from apps.todo.permissions import ToDoPermission
from rest_framework.permissions import AllowAny,IsAuthenticated
from apps.todo.models import ToDo
from apps.todo.serializers import ToDoSerializer

# Create your views here.
class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ToDoSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ToDoPermission(), )
        return (AllowAny(), )
    
class ToDoAllDelete(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
    def delete(self, request, *args, **kwargs):
        todo = ToDo.objects.filter(user=request.user)
        todo.delete()
        return Response({'delete' : 'Все такски удалены !!!!'})