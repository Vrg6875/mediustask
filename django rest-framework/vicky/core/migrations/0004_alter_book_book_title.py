# Generated by Django 4.2.13 on 2024-07-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_book_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=88),
        ),
    ]
