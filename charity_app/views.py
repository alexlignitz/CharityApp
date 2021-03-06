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
        quantity = request.POST.get('quantity')
        categories = request.POST.getlist('categories[]')
        institution = request.POST.get('institution')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        zip_code = request.POST.get('zip_code')
        pick_up_date = request.POST.get('pick_up_date')
        pick_up_time = request.POST.get('pick_up_time')
        pick_up_comment = request.POST.get('pick_up_comment')
        user = request.user
        donation = Donation.objects.create(quantity=quantity, institution_id=institution, address=address,
                                           city=city, phone_number=phone_number, zip_code=zip_code,
                                           pick_up_date=pick_up_date,
                                           pick_up_time=pick_up_time, pick_up_comment=pick_up_comment, user=user)
        for category in categories:
            donation.categories.add(category)
        donation.save()
        return render(request, 'form-confirmation.html')


class DonationConfirmation(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class DonationDetailsView(View):
    def get(self, request, id):
        donation = Donation.objects.get(id=id)
        return render(request, 'donation_details.html', {'donation': donation})


class DeleteDonationView(View):
    def get(self, request, id):
        return render(request, "change_confirmation.html", {
            'msg': 'Czy na pewno chcesz zrezygnowa?? z darowizny? Termin odbioru zostanie wtedy usuni??ty z naszego kalendarza.'})

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
            'msg': 'Czy darowizna zosta??a odebrana? '})

    def post(self, request, id):
        user = request.user
        if request.POST.get('answer') == 'Tak':
            donation = Donation.objects.get(id=id)
            donation.is_taken = True
            donation.closing_date = datetime.now()
            donation.save()
            return redirect('my_account', id=user.id)
        return redirect('donation_details', id=id)


class DonationNotTakenView(View):
    def get(self, request, id):
        return render(request, "change_confirmation.html", {
            'msg': 'Czy chcesz zmieni?? status darowizny na Nieodebrana? Nasza obs??uga klienta skontaktuje si?? wtedy z Tob?? w celu ustalenia nowego terminu odbioru'})

    def post(self, request, id):
        user = request.user
        if request.POST.get('answer') == 'Tak':
            donation = Donation.objects.get(id=id)
            donation.is_taken = False
            donation.closing_date = None
            donation.save()
            return redirect('my_account', id=user.id)
        return redirect('donation_details', id=id)
