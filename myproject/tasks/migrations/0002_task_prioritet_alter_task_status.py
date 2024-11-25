# Generated by Django 5.1.3 on 2024-11-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='prioritet',
            field=models.CharField(choices=[('low', 'Low'), ('middle', 'Middle'), ('hight', 'Hight')], default='low', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('grooming', 'Grooming'), ('in_progress', 'In Progress'), ('dev', 'Dev'), ('done', 'Done')], default='grooming', max_length=20),
        ),
    ]