# Generated by Django 4.2.3 on 2023-07-19 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_post_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
    ]