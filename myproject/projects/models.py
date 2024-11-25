from django.db import models
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
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_projects",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name