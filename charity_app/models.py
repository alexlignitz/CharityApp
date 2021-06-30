from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Category(models.Model):
    name = models.CharField(max_length=28)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'kategorie'
        verbose_name_plural = 'kategorie'


class Institution(models.Model):
    FOUNDATION = 1
    NGO = 2
    LOCAL = 3
    TYPE_CHOICES = [
        (FOUNDATION, 'Fundacja'),
        (NGO, 'Organizacja pozarządowa'),
        (LOCAL, 'Zbiórka lokalna'),
    ]

    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'instytucje'
        verbose_name_plural = 'instytucje'


def bag_amount():
    amount = Donation.objects.all().aggregate(Sum('quantity'))['quantity__sum']
    return amount


class Donation(models.Model):
    quantity = models.SmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=256, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    is_taken = models.BooleanField(default=False)
    closing_date = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'donacje'
        verbose_name_plural = 'donacje'


