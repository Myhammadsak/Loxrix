# Generated by Django 5.1.3 on 2024-11-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('arhive', 'Archive'), ('active', 'Active')], default='active', max_length=20),
        ),
    ]
