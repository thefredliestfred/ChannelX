from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            em = form.cleaned_data.get('email')
            uname = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {fname} {lname}!')
            send_mail(f'Welcome to ChannelX {uname}', f'{fname} {lname},\n Thank you for registering with ChannelX \n Your username is {uname}','WTAMU ChannelX', [ f'{em}',] )
            return redirect('main-thankyouregister')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user,)
#        p_form = ProfileUpdateForm(request.POST,
#                                   request.FILES,
#                                   instance=request.user.profile)
        if u_form.is_valid(): # and p_form.is_valid():
            u_form.save()
#            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
#        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
#        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
