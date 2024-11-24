from rest_framework import serializers
from .models import Project, User, ProjectParticipant


class ProjectParticipantSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ProjectParticipant
        fields = ['id', 'user', 'role']



class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'status', 'users', 'creator', 'created_at', 'updated_at']