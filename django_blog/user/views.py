from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import UserRegistrationForm

def registration(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created! You can now log in.')
            return redirect('login')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'form': registration_form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')