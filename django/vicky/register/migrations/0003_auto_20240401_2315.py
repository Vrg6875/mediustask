# Generated by Django 3.2.23 on 2024-04-01 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0002_auto_20240401_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
        migrations.AddField(
            model_name='register',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]