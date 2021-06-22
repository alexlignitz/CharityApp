from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts.forms import LoginForm
from accounts.views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegistrationView.as_view(), name='registration'),
]