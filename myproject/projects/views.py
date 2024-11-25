from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProjectSerializer
from .permissions import IsCreator
from rest_framework.permissions import IsAuthenticated
from .models import Project


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsCreator]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    lookup_field = 'id'

    filterset_fields = {
        'created_at': ['gte', 'lte'],
        'updated_at': ['gte', 'lte'],
    }

    ordering_fields = ['created_at', 'updated_at', 'name']
    ordering = ['created_at']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsCreator]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        return Project.objects.filter(status='active')
