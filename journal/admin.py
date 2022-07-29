from django.contrib import admin

# Register your models here.

# register your models here
from journal.models import Lesson, Grade, RatingItemStatus, GroupStudent, Score

admin.site.register(Lesson)
admin.site.register(Grade)
admin.site.register(RatingItemStatus)
#admin.site.register(GroupStudent)
admin.site.register(Score)