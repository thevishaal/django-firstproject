from django import forms
from student.models import Profile


'''class RegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        widget = forms.PasswordInput
    )'''

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField()

    class Meta:
        model = Profile
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Name:', 'email': 'Enter Email', 'password': 'Enter Password:'}
        error_messages = {
            'email': {'required': 'Email is required'},
            'password': {'required': 'Password is required'}
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'pwdclass'}),
            'name': forms.TextInput(attrs={'placeholder': 'yaha naam likhiye!'})
        }