from rest_framework import serializers
from .models import Task, Comment
from users.models import User
from projects.models import Project

class TaskSerializer(serializers.ModelSerializer):
    executor = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail',
        lookup_field='id'
    )
    tester = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name='user-detail',
        lookup_field='id'
    )
    project = serializers.HyperlinkedRelatedField(
        queryset=Project.objects.all(),
        view_name='project-detail',
        lookup_field='id',
    )

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'executor', 'tester', 'project',
            'deadline', 'created_at', 'updated_at', 'status', 'prioritet'
        ]


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'executor', 'tester', 'deadline', 'status', 'prioritet']




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'task', 'author', 'content', 'created_at']
        read_only_fields = ['author', 'created_at']