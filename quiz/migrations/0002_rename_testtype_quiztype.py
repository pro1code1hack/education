# Generated by Django 4.0.5 on 2022-07-04 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestType',
            new_name='QuizType',
        ),
    ]
