from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from charity_app.models import Institution, Category, Donation


class LadingPageView(View):
    def get(self, request):
        foundations = Institution.objects.filter(type=1)
        ngos = Institution.objects.filter(type=2)
        local_charities = Institution.objects.filter(type=3)
        categories = Category.objects.all()
        return render(request, '__base__.html',
                      {'foundations': foundations, 'ngos': ngos, 'local_charities': local_charities,
                       'categories': categories})


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'institutions': institutions})

    # def post(self, request):
    #     quantity = request.POST.get('bags')
    #     categories = request.POST.get('categories')
    #     institution = request.POST.get('organization')
    #     address = request.POST.get('address')
    #     city = request.POST.get('city')
    #     phone_number = request.POST.get('phone')
    #     zip_code = request.POST.get('postcode')
    #     pick_up_date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
    #     pick_up_time = datetime.strptime(request.POST.get('time'), '%H-%M').time()
    #     pick_up_comment = request.POST.get('more_info')
    #     donation = Donation(quantity=quantity, categories=categories, institution=institution, address=address,
    #                         city=city, phone_number=phone_number, zip_code=zip_code, pick_up_date=pick_up_date,
    #                         pick_up_time=pick_up_time, pick_up_comment=pick_up_comment)
    #     donation.save()
    #     return render(request, 'form-confirmation.html')