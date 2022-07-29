from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.

# ===================================================================================================================#
from django.urls import reverse_lazy

from education.settings import GENDER_CHOICES, USER_STATUS_CHOICES

AUTH_USER_MODEL = 'people.User'


class User(AbstractUser):
    """Пользователь."""
    middle_name = models.CharField('Отчество', max_length=130)
    sex = models.CharField('Пол', choices=GENDER_CHOICES, max_length=1)
    birth_date = models.DateField('Дата рождения', blank=True, null=True)
    photo = models.ImageField(upload_to='people/', default='static/img/default-user.png', blank=True)
    description = models.TextField('Характеристика')
    user_status = models.CharField('Статус пользователя', choices=USER_STATUS_CHOICES, max_length=15)       #TODO подумать над этим полем
    updated = models.DateField('Дата обновления', auto_now=True)
    university = models.ForeignKey('educational_institution.University', related_name='users', verbose_name='Университет', on_delete=models.SET_NULL, null=True, blank=True)
    education = models.TextField(default='')


    #group = models.ForeignKey('journal.GroupStudent', related_name='users', verbose_name='Класс', on_delete=models.SET_NULL, null=True, blank=True)
    #faculty = models.ForeignKey('educational_institution.Faculty', on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        # для того чтобы показать надстройки на админке
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Teacher(models.Model):
    """Учителя школы."""
    position = models.CharField('Должность', max_length=99)
    group_manager = models.ForeignKey('journal.GroupStudent', related_name='teacher', verbose_name='Руководит классом',
                                      on_delete=models.SET_NULL, null=True, blank=True)
    lessons = models.ManyToManyField('journal.Lesson', related_name='teachers', verbose_name='Ведет предметы')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE)
    years_of_experience = models.FloatField()
    about_experience = models.TextField()
    faculty = models.ForeignKey('educational_institution.Faculty', on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse_lazy('teacher_detail', kwargs={'pk': self.user_id})

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Student(models.Model):
    """Ученики школы."""
    group = models.ForeignKey('journal.GroupStudent', related_name='students', verbose_name='Состоит в классе',
                              on_delete=models.CASCADE)         # не на нашу группу
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE)
    education_form = models.CharField(max_length=100,
                                      choices=[('Full-Time', 'Full-Time'), ('Extramural', 'Extramural')])

    def get_absolute_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.user_id})

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'



# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100, default='')
#     age = models.IntegerField()
#     gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
#     university = models.ForeignKey('educational_institution.University', on_delete=models.CASCADE, blank=True,
#                                    null=True)
#     email = models.EmailField()
#     phone = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     profile_photo = models.ImageField(upload_to='people_photos/')
#     previous_education = models.TextField()
#     about = models.TextField()
#
#     def __str__(self):
#         return self.name



# ===================================================================================================================#
# class Teacher(Person, models.Model):
#     salary = models.FloatField()
#     years_of_experience = models.FloatField()
#     about_experience = models.TextField()
#     # publications = models.ForeignKey('Publications', on_delete=models.CASCADE, blank=True)
#     faculty = models.ForeignKey('educational_institution.Faculty', on_delete=models.CASCADE)
#     education = models.TextField(default='')
#     is_director = models.BooleanField(default=False)
#
class Test:
    pass

# # ===================================================================================================================#
# class Student(Person, models.Model):
#     group = models.ForeignKey('educational_institution.Group', on_delete=models.CASCADE)
#     # create the field education_form with the following choices: on-site, online
#     education_form = models.CharField(max_length=100,
#                                       choices=[('Full-Time', 'Full-Time'), ('Extramural', 'Extramural')])
#     course = models.IntegerField(choices=[(i, i) for i in range(1, 7)], default=1, blank=True, null=True)
#     budget_form = models.BooleanField(default=False)
# # ===================================================================================================================#
