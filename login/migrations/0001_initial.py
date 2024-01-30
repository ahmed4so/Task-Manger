# Generated by Django 5.0 on 2024-01-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=300)),
                ('Username', models.CharField(max_length=300)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=128)),
                ('Gender', models.CharField(choices=[('MALE', 'MALE'), ('Female', 'Female')], max_length=9)),
            ],
        ),
    ]
