# Generated by Django 5.0 on 2024-01-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_singup_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singup',
            name='Username',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]