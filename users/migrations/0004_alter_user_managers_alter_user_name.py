# Generated by Django 4.2 on 2024-07-22 14:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='user name', max_length=255, verbose_name='user-name'),
        ),
    ]
