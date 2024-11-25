from django.urls import path
from .views import CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('tasks/<int:task_id>/comments/', CommentListCreateAPIView.as_view(), name='task-comment-list-create'),
    path('comments/<int:id>/', CommentDetailAPIView.as_view(), name='task-comment-detail'),
]