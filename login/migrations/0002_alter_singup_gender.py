# Generated by Django 5.0 on 2024-01-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singup',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=9),
        ),
    ]
