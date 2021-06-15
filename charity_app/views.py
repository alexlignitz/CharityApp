from django.shortcuts import render
from django.views import View


class LadingPageView(View):
    def get(self, request):
        return render(request, '__base__.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


