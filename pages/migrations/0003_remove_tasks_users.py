# Generated by Django 5.0 on 2024-01-24 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_tasks_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='Users',
        ),
    ]
