from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            messages.success(request, f'Account created for {fname} {lname}!')
            return redirect('')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
