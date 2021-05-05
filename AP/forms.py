from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ArtWorkForm(forms.ModelForm):
    class Meta:
        model = ArtWork
        fields = ('name', 'cat', 'art', 'desc',)


class EditArtWorkForm(UpdateView):
    class Meta:
        model = ArtWork
        fields = ('name', 'cat', 'art', 'desc',)


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
