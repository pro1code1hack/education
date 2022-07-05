from django.contrib import admin
from .models import LessonVideos, LessonImages, AdditionalFiles, Lesson, Topic, Schedule

admin.site.register(LessonVideos)
admin.site.register(Topic)
admin.site.register(Schedule)


class LessonImagesInline(admin.TabularInline):
    model = LessonImages
    extra = 1


class LessonVideosInline(admin.TabularInline):
    model = LessonVideos
    extra = 1


class AdditionalFilesInline(admin.TabularInline):
    model = AdditionalFiles
    extra = 1


class TopicInline(admin.TabularInline):
    model = Topic


# Этот код написан, для удобства взаимодействия с моделью Lesson, мы по факту склеиваем Lesson с видео и картинками
class LessonsAdmin(admin.ModelAdmin):
    inlines = [LessonImagesInline, LessonVideosInline, AdditionalFilesInline]


admin.site.register(Lesson, LessonsAdmin)
