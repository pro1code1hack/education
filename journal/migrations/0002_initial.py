# Generated by Django 4.0.5 on 2022-07-29 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('journal', '0001_initial'),
        ('educational_institution', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(limit_choices_to={'user_status': 'student'}, on_delete=django.db.models.deletion.CASCADE, related_name='score_student', to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='score',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'user_status': 'teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='score_teacher', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='grade',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='journal.grade', verbose_name='Наименование класса'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='specialty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='educational_institution.specialty'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='subjects',
            field=models.ManyToManyField(to='educational_institution.subject'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='educational_institution.university'),
        ),
        migrations.AddField(
            model_name='grade',
            name='lessons',
            field=models.ManyToManyField(related_name='grade', to='journal.lesson', verbose_name='Уроки класса'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('student', 'lesson', 'created')},
        ),
    ]
