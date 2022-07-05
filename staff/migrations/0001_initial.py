# Generated by Django 4.0.5 on 2022-07-03 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educational_institution', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(upload_to='people/')),
                ('previous_education', models.TextField()),
                ('about', models.TextField()),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='educational_institution.university')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.person')),
                ('salary', models.FloatField()),
                ('years_of_experience', models.FloatField()),
                ('about_experience', models.TextField()),
                ('education', models.TextField()),
                ('is_director', models.BooleanField(default=False)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educational_institution.faculty')),
            ],
            bases=('staff.person', models.Model),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.person')),
                ('education_form', models.CharField(max_length=100)),
                ('course', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1, null=True)),
                ('budget_form', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educational_institution.group')),
            ],
            bases=('staff.person', models.Model),
        ),
    ]