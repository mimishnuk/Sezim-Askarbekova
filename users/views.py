from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.userforms import LogingForm, RegisterForm
from django.contrib.auth.models import User
# Create your views here.


def login_view(request):
    if request.method == "GET":
        context = {
            'form': LogingForm
        }

        return render(request, 'users/login.html', context=context)

    if request.method == 'POST':
        form = LogingForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user=user)
                return redirect('/products/')

            else:
                form.add_error('username', 'bad request')

        return render(request, 'users/login.html', context={
            'form': form
        })

def logout_view(request):
    logout(request)
    return redirect('/products/')


def register_view(request):
    if request.method == "GET":
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password2')
                )
                login(request, user)
                return redirect('/products/')

            else:
                form.add_error("password2", 'bad request!')

            return render(request, 'users/register.html', context={
                'form': form
            })




















