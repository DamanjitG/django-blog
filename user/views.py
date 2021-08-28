from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

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
    if request.method == 'POST':
        u_update_form = UserUpdateForm(request.POST, instance=request.user)
        p_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_update_form.is_valid() and p_update_form.is_valid():
            u_update_form.save()
            p_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_update_form = UserUpdateForm(instance=request.user)
        p_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_update_form': u_update_form,
        'p_update_form': p_update_form
    }

    return render(request, 'user/profile.html', context)