from django.db import models
from staff.models import Teacher
# Student

# ====================================================================================================================#
class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # faculties = models.ManyToManyField('Faculty')
    about = models.TextField()

    # teachers = models.ManyToManyField('Teacher')

    def __str__(self):
        return self.name


# ====================================================================================================================#
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    university = models.ForeignKey('University', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# ====================================================================================================================#


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    # groups = models.ManyToManyField('Group')
    # subjects = models.ManyToManyField('Subject')
    years_to_study = models.IntegerField()
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


# ====================================================================================================================#

class Subject(models.Model):
    name = models.CharField(max_length=100)
    credit_score = models.IntegerField()
    scholarship_impact = models.BooleanField()
    hours = models.IntegerField()
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, blank=True, null=True)
    subject_type = models.ForeignKey('SubjectType', on_delete=models.CASCADE)
    hours_for_year = models.IntegerField(blank=True, null=True)
    #days_per_week = models.IntegerField()   #TODO ПОДУМАТЬ
    course = models.IntegerField(choices=[(i, i) for i in range(1, 7)], blank=True, null=True)

    def __str__(self):
        return self.name


class SubjectType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ====================================================================================================================#


# ====================================================================================================================#
# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, blank=True, null=True)
#     subjects = models.ManyToManyField('Subject')
#     # teachers = models.ManyToManyField('staff.Teacher', blank=True, null=True) #TODO переделать потом
#     university = models.ForeignKey('University', on_delete=models.CASCADE, blank=True, null=True)
#     course = models.IntegerField(choices=[(i, i) for i in range(1, 7)], default=1, blank=True, null=True)
#
#     # students = models.ManyToManyField('Student')
#
#     def __str__(self):
#         return self.name
#

