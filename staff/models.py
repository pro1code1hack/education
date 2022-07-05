from django.db import models


# Create your models here.

# ===================================================================================================================#
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    university = models.ForeignKey('educational_institution.University', on_delete=models.CASCADE, blank=True,
                                   null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='people/')
    previous_education = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name


# ===================================================================================================================#
class Teacher(Person, models.Model):
    salary = models.FloatField()
    years_of_experience = models.FloatField()
    about_experience = models.TextField()
    # publications = models.ForeignKey('Publications', on_delete=models.CASCADE, blank=True)
    faculty = models.ForeignKey('educational_institution.Faculty', on_delete=models.CASCADE)
    education = models.TextField()
    is_director = models.BooleanField(default=False)


# ===================================================================================================================#
class Student(Person, models.Model):
    group = models.ForeignKey('educational_institution.Group', on_delete=models.CASCADE)
    # create the field education_form with the following choices: on-site, online
    education_form = models.CharField(max_length=100,
                                      choices=[('Full-Time', 'Full-Time'), ('Extramural', 'Extramural')])
    course = models.IntegerField(choices=[(i, i) for i in range(1, 7)], default=1, blank=True, null=True)
    budget_form = models.BooleanField(default=False)
# ===================================================================================================================#
