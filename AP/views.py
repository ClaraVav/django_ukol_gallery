from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import *
from .models import *


# Create your views here.
def main_page(request):
    cats = Category.objects.order_by('-name')
    works = ArtWork.objects.order_by('-name')
    return render(request, 'AP/mainpage.html', {'cats': cats, 'works': works})


def art_list(request):
    works = ArtWork.objects.order_by('-name')
    return render(request, 'AP/artlist.html', {'works': works})


def art_detail(request, pk):
    art = get_object_or_404(ArtWork, pk=pk)
    return render(request, 'AP/artdetail.html', {'art': art})


@login_required
def upload(request):
    return render(request, 'AP/artcreate.html')


def cat_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    artworks = ArtWork.objects.order_by('-name')
    return render(request, 'AP/categorydetail.html', {'category': category, 'artworks': artworks})


def cat_create(request):
    return render(request, 'AP/categorycreate.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password1')
        if form.is_valid:
            userdata = form.save()
            userguy = authenticate(username=name, password=passw)
            userdata.save()
            try:
                login(request, userguy)
            except AttributeError:
                messages.error(request, 'Chyba při přihlašování u registrace')
                return redirect('/register')
            return redirect('/')
        else:
            messages.error(request, 'Chyba při registraci')
    else:
        form = RegisterForm()
    return render(request, 'AP/register.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password')
        if form.is_valid:
            userdata = authenticate(username=name, password=passw)
            try:
                login(request, userdata)
            except AttributeError:
                messages.error(request, 'Nesprávné jméno nebo heslo')
                return redirect('/login')
            return redirect('/')
        else:
            messages.error(request, 'Chyba při přihlášení')
    else:
        form = LoginForm()
    return render(request, 'AP/login.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('/')


@login_required
def profile_page(request):
    artworks = ArtWork.objects.order_by('-name')
    return render(request, 'AP/profilepage.html', {'artworks': artworks})

# Color palette: https://coolors.co/bee9e8-62b6cb-1b4965-cae9ff-5fa8d3
