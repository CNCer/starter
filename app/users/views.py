from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from .forms import UserUpdateForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import  reverse
from django.conf import settings
from django.contrib.auth.decorators import login_not_required
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate
from django.contrib import messages

# Create your views here.

def addCookiesToResponce(response, user):
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME,
        user.profile.language,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    response.set_cookie(
        settings.THEME_COOKIE_NAME,
        user.profile.theme,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
   
    return response


def createUserCookies(request, user):
    next_url = "/"

    #response = HttpResponseRedirect('/') 
    lang_code = user.profile.language
    activate(lang_code)
    response = redirect('/')
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME,
        lang_code,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    response.set_cookie(
        settings.THEME_COOKIE_NAME,
        user.profile.theme,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
   
    return response

@login_not_required
def login_ (request):
    if request.user.is_authenticated:
        if request.META.get('HTTP_REFERER') :
            return redirect(request.META.get('HTTP_REFERER'))
        else :
            return redirect(reverse('dashboard:index'))
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username_v = form.cleaned_data['username']
            password_v = form.cleaned_data['password']
            user = authenticate(request, username = username_v, password = password_v)
            if user is not None:
                login(request, user)
                activate(user.profile.language)
                return addCookiesToResponce(redirect(reverse('dashboard:index')), user) 
    else :
         form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_(request):
    logout(request)
    return redirect(reverse('user:login'))

def userProfileEdit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,  instance = request.user)
        profile_form = UserProfileForm(request.POST, request.FILES  ,instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, _('Profile successfuly updated.'))
            activate(request.user.profile.language)
            return addCookiesToResponce(redirect(reverse('dashboard:index')), request.user)
            

    else :
        user_form = UserUpdateForm(instance = request.user)
        profile_form = UserProfileForm(instance = request.user.profile)



    context = {
        'u_form' : user_form,
        'p_form' : profile_form,
    }
    return render(request, 'users/profile.html', context)

def changePassword(request):
    if request.method == 'POST':
        currentUser = request.user
        #form = PasswordChangeForm(request.POST,  instance = request.user)
        form = PasswordChangeForm(user =  request.user,  data = request.POST)
        if form.is_valid() :
            form.save()
            login(request, currentUser)
            messages.success(request, _('Password successfuly updated.'))
            #return redirect(request,'dashboard.index')
            return redirect(reverse('dashboard:index'))
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/changePassword.html', {'form':form})