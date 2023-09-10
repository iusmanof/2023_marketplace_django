from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=({
            'placeholder': 'Your username',
            'class': 'my_class'
    })))

    password = forms.CharField(widget=forms.PasswordInput(attrs=({
            'placeholder': 'Your password',
            'class': 'my_class'
    })))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs=({
            'placeholder': 'Your username',
            'class': 'my_class'
    })))

    email = forms.CharField(widget=forms.EmailInput(attrs=({
            'placeholder': 'Your email address',
            'class': 'my_class'
    })))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs=({
            'placeholder': 'Your password',
            'class': 'my_class'
    })))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=({
            'placeholder': 'Repeat password',
            'class': 'my_class'
    })))