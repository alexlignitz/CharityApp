from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from charity_app.models import Institution, Category, Donation, bag_amount


class LadingPageView(View):
    def get(self, request):
        foundations = Institution.objects.filter(type=1)
        ngos = Institution.objects.filter(type=2)
        local_charities = Institution.objects.filter(type=3)
        categories = Category.objects.all()
        bags = bag_amount()
        donations = len(Donation.objects.all().values('institution').distinct())
        return render(request, '__base__.html',
                      {'foundations': foundations, 'ngos': ngos, 'local_charities': local_charities,
                       'categories': categories, 'bags': bags, 'donations': donations})


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'institutions': institutions})

    def post(self, request):
        quantity = request.POST.get('bags')
        categories = request.POST.get('categories')
        institution = request.POST.get('organization')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone')
        zip_code = request.POST.get('postcode')
        pick_up_date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
        pick_up_time = datetime.strptime(request.POST.get('time'), '%H-%M').time()
        pick_up_comment = request.POST.get('more_info')
        user = request.user
        donation = Donation(quantity=quantity, institution=institution, address=address,
                            city=city, phone_number=phone_number, zip_code=zip_code, pick_up_date=pick_up_date,
                            pick_up_time=pick_up_time, pick_up_comment=pick_up_comment, user=user)
        donation.save(commit=False)
        for category in categories:
            donation.categories.add(category)
        donation.save()
        return render(request, 'form-confirmation.html')


class DonationDetailsView(View):
    def get(self, request, id):
        donation = Donation.objects.get(id=id)
        return render(request, 'donation_details.html', {'donation': donation})


class DeleteDonationView(View):
    def get(self, request, id):
        return render(request, "change_confirmation.html", {
            'msg': 'Czy na pewno chcesz zrezygnować z darowizny? Termin odbioru zostanie wtedy usunięty z naszego kalendarza.'})

    def post(self, request, id):
        user = request.user
        if request.POST.get('answer') == 'Tak':
            donation = Donation.objects.get(id=id)
            donation.delete()
            return redirect('my_account', id=user.id)
        return redirect('donation_details', id=id)


class DonationTakenView(View):
    def get(self, request, id):
        return render(request, "change_confirmation.html", {
            'msg': 'Czy darowizna została odebrana? '})

    def post(self, request, id):
        if request.POST.get('answer') == 'Tak':
            donation = Donation.objects.get(id=id)
            donation.is_taken = True
            donation.save()
            return redirect('donation_details', id=id)
        return redirect('donation_details', id=id)


class DonationNotTakenView(View):
    def get(self, request, id):
        return render(request, "change_confirmation.html", {
            'msg': 'Czy chcesz zmienić status darowizny na Nieodebrana? Nasza obsługa klienta skontaktuje się wtedy z Tobą w celu ustalenia nowego terminu odbioru'})

    def post(self, request, id):
        if request.POST.get('answer') == 'Tak':
            donation = Donation.objects.get(id=id)
            donation.is_taken = False
            donation.save()
            return redirect('donation_details', id=id)
        return redirect('donation_details', id=id)
