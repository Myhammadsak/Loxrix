# Generated by Django 5.1.3 on 2024-11-24 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_status'),
        ('users', '0004_delete_projectparticipant'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='project_history',
            field=models.ManyToManyField(blank=True, related_name='history_users', to='projects.project'),
        ),
    ]
