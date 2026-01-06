from django import forms
from school.models import Profile


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['student_name', 'email', 'password']


class TeacherRegistrationForm(StudentRegistrationForm):
    class Meta(StudentRegistrationForm.Meta):
        fields = ['teacher_name', 'email', 'password']
        