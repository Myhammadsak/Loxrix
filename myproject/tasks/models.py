from django.db import models
from django.conf import settings
from projects.models import Project

class Task(models.Model):
    STATUS_CHOICES = [
        ('grooming', 'Grooming'),
        ('in_progress', 'In Progress'),
        ('dev', 'Dev'),
        ('done', 'Done'),
    ]

    VIP_CHOICES = [
        ('low', 'Low'),
        ('middle', 'Middle'),
        ('hight', 'Hight')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    executor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks_executor')
    tester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks_tester')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='grooming')
    prioritet = models.CharField(max_length=20, choices=VIP_CHOICES, default='low')

    def __str__(self):
        return self.title

    def mark_as_completed(self):
        self.status = 'completed'
        self.save()

    def mark_as_closed(self):
        self.status = 'closed'
        self.save()

    class Meta:
        ordering = ['-created_at']



class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on Task {self.task.id}"
