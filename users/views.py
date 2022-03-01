from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('blog-home')

    if request.method == "GET":
        form = UserRegisterForm()
    elif request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'{username} successfully signed up')
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        userForm = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, f'{request.user.username} successfully updated profile page')
            return redirect('profile')
    elif request.method == "GET":
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)


    return render(request, "users/profile.html", {'userForm': userForm, 'profileForm': profileForm})