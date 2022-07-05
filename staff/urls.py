from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.TeachersView.as_view(), name='teachers'),     # сдесь будут все учителя

    # path('teachers/', views.teachers, name='teachers'),
    # path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    # path('students/', views.students, name='students'),
    # path('students/<int:student_id>/', views.student_detail, name='student_detail'),
]
