from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from student.models import Profile

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            passw = form.cleaned_data['password']
            # print("Name:",name)
            # print("Email:",email)
            # print("Password:",password)
            # Save data into database
            user = Profile(name = nm, email = em, password = passw)
            user.save()
            # user update
            # user = Profile(id=1, name = nm, email = em, password = passw)
            # user.save()
            return HttpResponseRedirect('/student/success/')
    else:
        form = RegistrationForm()
    return render(request, "student/register.html", {'form': form})


def reg_success(request):
    return render(request, "student/succes.html")