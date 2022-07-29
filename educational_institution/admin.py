from django.contrib import admin

from journal.models import GroupStudent
from .models import University, Faculty, Specialty, Subject, SubjectType

class SubjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_type', 'faculty')
    list_filter = ('name', 'subject_type', 'faculty')
    search_fields = ('name', 'subject_type', 'faculty')
    ordering = ('name',)


# create Tabular inline for Subject
class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0


admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Specialty)
admin.site.register(GroupStudent)
admin.site.register(SubjectType, SubjectTypeAdmin)
admin.site.register(Subject, SubjectAdmin)

