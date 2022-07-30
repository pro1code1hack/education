from django.contrib import admin

# Register your models here.
from quiz.models import Quiz, Question, Answer, Result, QuizType


# admin.site.register(QuizType)
# admin.site.register(Quiz)
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Result)


# Create tabular inline for Question, Answer, Result, QuizType

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)


# ----------------------------------------------------------------------------------------------------------------------
class ResultInline(admin.TabularInline):
    model = Result
    extra = 1

# ResultInline

# class QuizAdmin(admin.ModelAdmin):
#     inlines = [QuestionInline]  # TODO продумать генерацию отчётов и журналов!


admin.site.register(Quiz)
admin.site.register(QuizType)