from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.forms import LoginForm
from accounts.views import RegistrationView, LoginView, LogoutView, MyAccountView, SettingsView, PasswordAuthView

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('my_account/<int:id>/', MyAccountView.as_view(), name="my_account"),
    path('settings/<int:id>/', SettingsView.as_view(), name="settings"),
    path('password_auth/<int:id>/', PasswordAuthView.as_view(), name="password_auth"),

    # PASSWORD CHANGE
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name="password_change"),
    path('change_password_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_complete.html"),
         name="password_change_done"),
]
