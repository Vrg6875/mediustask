# Generated by Django 3.2.23 on 2024-02-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_vic_ekaur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_vic',
            name='ekaur',
        ),
        migrations.AddField(
            model_name='project_vic',
            name='goal',
            field=models.TextField(default='mera'),
        ),
    ]
