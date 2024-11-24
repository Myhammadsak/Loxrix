from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminOrSelf

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf]

    def get_queryset(self):
        return User.objects.all()

    def perform_update(self, serializer):
        if 'role' in self.request.data and self.request.user.role != 'admin':
            raise PermissionError("Вы не можете изменять роль пользователя.")
        serializer.save()

    def perform_create(self, serializer):
        if not serializer.validated_data.get('avatar'):
            serializer.validated_data['avatar'] = 'avatars/default_avatar.png'
        serializer.save()