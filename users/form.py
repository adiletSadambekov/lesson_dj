from cgitb import text
from enum import unique
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUsers(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    

class AddArticle(forms.Form):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'form_title_article'}))
    text = forms.CharField(label='text', max_length=500, widget=forms.TextInput(attrs={'class': 'form_text_article'}))


