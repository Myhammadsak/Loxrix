# Generated by Django 5.1.3 on 2024-11-24 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_project_projectparticipant'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectParticipant',
        ),
    ]