# Generated by Django 5.0 on 2024-01-24 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_tasks_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='User',
            new_name='User_name',
        ),
    ]
