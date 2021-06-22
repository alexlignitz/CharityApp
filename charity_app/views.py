from django.shortcuts import render
from django.views import View

from charity_app.models import Institution, Category


class LadingPageView(View):
    def get(self, request):
        foundations = Institution.objects.filter(type=1)
        ngos = Institution.objects.filter(type=2)
        local_charities = Institution.objects.filter(type=3)
        categories = Category.objects.all()
        return render(request, '__base__.html',
                      {'foundations': foundations, 'ngos': ngos, 'local_charities': local_charities,
                       'categories': categories})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')
