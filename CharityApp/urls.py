from django.contrib import admin
from django.urls import path, include

from charity_app.views import LadingPageView, AddDonationView, DonationDetailsView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    path('', LadingPageView.as_view(), name="landing"),
    path('add_donation/', AddDonationView.as_view(), name="add_donation"),
    path('donation_details/<int:id>/', DonationDetailsView.as_view(), name="donation_details"),
]
