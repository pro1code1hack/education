# Generated by Django 4.0.5 on 2022-07-04 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
    ]
