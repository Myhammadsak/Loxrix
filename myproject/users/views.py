from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from users.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    lookup_field = 'id'

    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
        if not serializer.validated_data.get('avatar'):
            serializer.validated_data['avatar'] = 'avatars/Без имени.jpg'
        serializer.save()