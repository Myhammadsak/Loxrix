from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProjectSerializer
from .models import Project


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    lookup_field = 'id'

    filterset_fields = {
        'created_at': ['gte', 'lte'],
        'updated_at': ['gte', 'lte'],
    }

    ordering_fields = ['created_at', 'updated_at', 'name']
    ordering = ['created_at']


    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset