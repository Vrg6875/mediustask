# Generated by Django 3.2.23 on 2024-02-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_vic_another'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_vic',
            name='ekaur',
            field=models.TextField(default='kutta'),
        ),
    ]
