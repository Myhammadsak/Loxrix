from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    WORK_CHOICES = (
        ('analyst', 'Analyst'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'Devops'),
        ('tester', 'Tester'),
        ('designer', 'Designer'),
        ('project_manager', 'Project manager'),
        ('conzept', 'Conzept'),
        ('non', 'Non'),
    )
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    work_role = models.CharField(max_length=20, choices=WORK_CHOICES, default='non')

    def __str__(self):
        return self.username


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name="owned_projects"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)