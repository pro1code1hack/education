from django.core.validators import FileExtensionValidator
from django.db import models

# create the class Lesson with the following structure
from django.utils import timezone

from lessons.utils import get_lesson_file

"""
tittle
subject(FK)
teacher(FK)
main_text 
post_photos [array]
video - link ( video hosting)
additional text
group(FK)
Topic(FK)
"""
"""
Поля моделі  Topic 
topic_name 
amount_of_hours
description
subject (FK) 

"""


# ===================================================================================================================#
class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    amount_of_hours = models.IntegerField()
    description = models.TextField()
    subject = models.ForeignKey('educational_institution.Subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name


# ===================================================================================================================#
class Lesson(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    # subject = models.ForeignKey('educational_institution.Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('staff.Teacher', on_delete=models.CASCADE)
    main_text = models.TextField()
    additional_text = models.TextField()
    group = models.ForeignKey('educational_institution.Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.topic.topic_name


# ===================================================================================================================#
class LessonImages(models.Model):
    lesson = models.ForeignKey(Lesson, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_lesson_file,
                              verbose_name='Image',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    date_uploaded = models.DateTimeField(default=timezone.now)


# ===================================================================================================================#
class LessonVideos(models.Model):
    lesson = models.ForeignKey(Lesson, default=None, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.video


# ===================================================================================================================#

class AdditionalFiles(models.Model):
    lesson = models.ForeignKey(Lesson, default=None, on_delete=models.CASCADE)
    video = models.FileField(upload_to='lesson_files_upload', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['doc', 'pptx', 'xls', 'csv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)


class Schedule(models.Model):
    subject = models.ForeignKey('educational_institution.Subject', on_delete=models.CASCADE)
    group = models.ForeignKey('educational_institution.Group', on_delete=models.CASCADE, blank=True, null=True)
    day = models.CharField(max_length=10, choices=(
        ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'),
        ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')))
    time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.subject} : {self.group} : {self.day} : {self.time}'
