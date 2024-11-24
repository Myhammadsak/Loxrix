from django.db import models
from django.conf import settings
from users.models import User

class Project(models.Model):
    STATUS_CHOICES = {
        ('active', 'Active'),
        ('arhive', 'Archive')
    }
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    users = models.ManyToManyField(User, related_name='projects')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectParticipant(models.Model):

    ROLE_CHOICES = [
        ('non', 'Non'),
        ('analyst', 'Analyst'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('project-manager', 'Project-manager'),
        ('designer', 'Designer'),
        ('conceptologist', 'Conceptologist'),
        ('devops', 'Devops'),
        ('tester', 'Tester')
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_participants')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_projects')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='non')

    class Meta:
        unique_together = ('project', 'user')