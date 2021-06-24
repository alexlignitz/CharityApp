from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import RegistrationForm, LoginForm


class LoginView(View):
    def get(self, request):
        print("jako")
        return render(request, 'registration/login.html')

    def post(self, request):
        users = User.objects.all()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            if user not in users:
                return redirect('registration')
        return HttpResponse('Nieprawidłowy email i/lub hasło')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(email=email, username=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})
