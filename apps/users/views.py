from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from apps.users.permissions import UserPermission
from rest_framework.permissions import AllowAny,IsAuthenticated
from apps.users.models import User 
from apps.users.serializers import UserRegisterSerializer, UserSerializers,UserDetailSerializer

# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated, )
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        
    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializers
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermission(), )
        return (AllowAny(), )