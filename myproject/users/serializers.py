from rest_framework import serializers
from .models import User
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email',
                   'work_role', 'projects', 'avatar']
        read_only_fields = ['id']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.work_role = validated_data.get('work_role', instance.work_role)
        instance.save()
        return instance

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        if obj.avatar and request:
            return request.build_absolute_uri(obj.avatar.url)
        return None