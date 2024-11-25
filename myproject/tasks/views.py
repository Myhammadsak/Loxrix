from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import TaskSerializer, TaskUpdateSerializer
from rest_framework.filters import OrderingFilter
from rest_framework import permissions, status
from rest_framework.response import Response
from tasks.models import Task, Comment
from tasks.serializers import CommentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'created_at': ['gte', 'lte'],
        'updated_at': ['gte', 'lte'],
        'status': ['exact'],
        'executor': ['exact'],
        'prioritet': ['exact']
    }
    ordering_fields = ['created_at', 'updated_at', 'title', 'status', 'executor', 'prioritet']
    ordering = ['-created_at']

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskUpdateSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()



class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = Task.objects.get(id=self.kwargs['task_id'])
        serializer.save(author=self.request.user, task=task)

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_id'])

class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'