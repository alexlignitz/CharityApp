from django.contrib import admin
from django.urls import path, include

from charity_app.views import LadingPageView, AddDonationView, DonationDetailsView, DeleteDonationView, \
    DonationTakenView, DonationNotTakenView, DonationConfirmation

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    path('', LadingPageView.as_view(), name="landing"),
    path('add_donation/', AddDonationView.as_view(), name="add_donation"),
    path('donation_confirmation', DonationConfirmation.as_view(), name="donation_confirmation"),
    path('donation_details/<int:id>/', DonationDetailsView.as_view(), name="donation_details"),
    path('donation_delete/<int:id>/', DeleteDonationView.as_view(), name="donation_delete"),
    path('donation_taken/<int:id>/', DonationTakenView.as_view(), name="donation_taken"),
    path('donation_not_taken/<int:id>/', DonationNotTakenView.as_view(), name="donation_not_taken"),
]
