# Generated by Django 3.2.23 on 2024-04-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_register_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
        migrations.AddField(
            model_name='register',
            name='first_name',
            field=models.CharField(default='', max_length=89),
        ),
        migrations.AddField(
            model_name='register',
            name='last_name',
            field=models.CharField(default='', max_length=89),
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default='', max_length=89),
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default='', max_length=89),
        ),
    ]
