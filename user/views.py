from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form= CustomUserCreationForm(request.POST)
    else:
        form = CustomUserCreationForm()
        
    return render(request, "registration/register.html", {"form": form})  # Added missing comma
