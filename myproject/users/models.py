from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    project_history = models.ManyToManyField('projects.Project', related_name='history_users', blank=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'admin'
        super().save(*args, **kwargs)

    @classmethod
    def create_superuser(cls, *args, **kwargs):
        kwargs['role'] = 'admin'
        return super().create_superuser(*args, **kwargs)


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