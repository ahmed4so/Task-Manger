# Generated by Django 5.0 on 2024-01-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_rename_userprofile_singup'),
    ]

    operations = [
        migrations.AddField(
            model_name='singup',
            name='fullname',
            field=models.CharField(default='nono', max_length=1000),
            preserve_default=False,
        ),
    ]
