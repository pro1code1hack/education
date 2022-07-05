from django.contrib import admin

from educational_institution.admin import SubjectInline
from .models import Teacher, Student




#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = (
#         'name', 'faculty', 'city', 'email', 'experience', 'about', 'profile_photo', 'group', 'budget_form')
#     list_filter = (
#         'faculty', 'city', 'email', 'experience', 'about', 'profile_photo', 'group', 'budget_form')
#     search_fields = (
#         'name', 'faculty', 'city', 'email', 'experience', 'about', 'profile_photo', 'group', 'budget_form')
#     ordering = ('name', 'faculty', 'city', 'email', 'experience', 'about', 'profile_photo', 'group', 'budget_form')
#     filter_horizontal = ('group',)
#     filter_vertical = ('group',)
#     raw_id_fields = ('group',)
#     fieldsets = (
#         ('Main', {
#             'fields': (
#                 'name', 'faculty', 'city', 'email', 'experience', 'about', 'profile_photo', 'group', 'budget_form')
#         }),
#     )
#     inlines = [SubjectInline]
#     prepopulated_fields = {'slug': ('name',)}
#     autocomplete_fields = ('group',)
#     date_hierarchy = 'date'
#     exclude = ('date_added', 'date_updated')
#     save_on_top = True
#     save_as = True
#     show_full_result_count = True
#     show_change_link = True


admin.site.register(Teacher)
admin.site.register(Student)
