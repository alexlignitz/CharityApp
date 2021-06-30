from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import RegistrationForm, LoginForm
from charity_app.models import Donation, Category


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if not User.objects.filter(username=username).exists():
                return redirect('registration')
            if user is not None:
                login(request, user)
                return redirect('my_account', id=user.id)
        return render(request, 'registration/login.html', {'msg': 'Nieprawidłowy email i/lub hasło'})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')


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


class MyAccountView(LoginRequiredMixin, View):
    def get(self, request, id):
        donations = Donation.objects.filter(user_id=id).order_by('is_taken').order_by('-closing_date')
        categories = Category.objects.all()
        return render(request, 'my_account.html', {'donations': donations, 'categories': categories})
