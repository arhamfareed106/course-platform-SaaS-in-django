from tkinter import Widget
from turtle import width
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email= forms.EmailFeild(required=True, Widget= forms.EmailInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        feild = ("Username", "email", "password1", "password2")