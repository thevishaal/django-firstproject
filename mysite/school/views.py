from django.shortcuts import render
from school.forms import StudentRegistrationForm, TeacherRegistrationForm

# Create your views here.
def student_form_view(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentRegistrationForm()
    return render(request, "school/studentreg.html", {'form': form})


def teacher_form_view(request):
    if request.method == "POST":
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherRegistrationForm()
    return render(request, "school/teacherreg.html", {'form': form})