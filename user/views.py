import re
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("course")  # Use URL name instead of hardcoding the path
    else:
        form = CustomUserCreationForm()
        
    return render(request, "registration/register.html", {"form": form})
