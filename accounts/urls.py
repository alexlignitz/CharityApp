from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.forms import LoginForm
from accounts.views import RegistrationView, LoginView, LogoutView, MyAccountView

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('my_account/<int:id>', MyAccountView.as_view(), name="my_account"),
]