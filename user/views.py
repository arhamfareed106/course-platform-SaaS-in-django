# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/course")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})

def custom_logout(request):
    logout(request)  # Log out the user
    return redirect('register')  # Redirect to the registration page
