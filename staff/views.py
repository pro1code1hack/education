from django.shortcuts import render, redirect

# Create your views here.

# write the class-based view for the teachers page --> select all teachers and the specific one
from django.views import View

from .forms import TeacherForm
from staff.models import Teacher


class TeachersView(View):
    def get(self, request, pk=None):
        if pk:
            teacher = Teacher.objects.get(id=pk)
            form = TeacherForm(instance=teacher)
            return render(request, 'staff/profile.html', {'teacher': teacher, 'form': form})
        return render(request, 'staff/teachers.html', {'teachers': Teacher.objects.all()})

    def post(self, request, pk=None):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            # save updated data to the database
            print(form.cleaned_data)
            teacher = Teacher.objects.update(form.cleaned_data)
            teacher.save()
            return redirect('/')
        return render(request, 'staff/profile.html', {'form': form})
# def index(request):
#    return render(request, 'profile.html')
