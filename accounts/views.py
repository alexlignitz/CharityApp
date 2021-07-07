from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
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
        donations_taken = Donation.objects.filter(user_id=id, is_taken=True).order_by('closing_date')
        donations_open = Donation.objects.filter(user_id=id, is_taken=False).order_by('pick_up_date')
        categories = Category.objects.all()
        return render(request, 'my_account.html', {'donations_taken': donations_taken, 'donations_open': donations_open, 'categories': categories})


class SettingsView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        return render(request, 'settings.html', {'user': user})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = email
        user.save()
        return redirect('my_account', id=user.id)


class PasswordAuthView(LoginRequiredMixin, View):
    def get(self, request, id):
        return render(request, 'password_authentication.html')

    def post(self, request, id):
        user = User.objects.get(pk=id)
        password = request.POST.get('password')
        pass_to_check = make_password(password)
        verification = check_password(password, pass_to_check)
        if verification:
            return redirect('settings', id=user.id)