from django.core.mail import send_mail
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

    def perform_create(self, serializer):
        instance = serializer.save()
        for user in instance.users.all():
            # send_mail(
            #     subject="Вы добавлены в проект",
            #     message=f"Здравствуйте, {user.username}! Вы были добавлены в проект '{instance.name}'.",
            #     from_email="jamalsigma11@gmail.com",  # Укажите ваш email
            #     recipient_list=[user.email],
            #     fail_silently=False,  # Чтобы исключения поднимались при ошибках
            # )
            print(f"дравствуйте, {user.username}! Вы были добавлены в проект '{instance.name}'")

    def perform_update(self, serializer):
        instance = self.get_object()
        previous_users = set(instance.users.all())
        instance = serializer.save()
        current_users = set(instance.users.all())
        new_users = current_users - previous_users

        for user in new_users:
            # send_mail(
            #     subject="Вы добавлены в проект",
            #     message=f"Здравствуйте, {user.username}! Вы были добавлены в проект '{instance.name}'.",
            #     from_email="jamalsigma11@gmail.com",
            #     recipient_list=[user.email],
            #     fail_silently=False,
            # )
            print(f"дравствуйте, {user.username}! Вы были добавлены в проект '{instance.name}'")