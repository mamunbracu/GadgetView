
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
#forms and model

from App_Login.models import Profile
from App_Login.forms import SignUpForm, ProfileForm


# Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

#messsage
from django.contrib import messages
# Create your views here.


def sign_up(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Sign Up Successful")
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/signup.html', context={'title':'SignUp', 'form':form})


def login_page(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request, 'App_Login/login.html', context={'title':'Login', 'form':form})


@login_required

def logout_page(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def userProfile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile saved")
            return HttpResponseRedirect(reverse('App_Shop:home'))

    return render(request, 'App_Login/change_profile.html', context={'title':'Profile', 'form':form})



