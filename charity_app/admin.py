from django.contrib import admin

# Register your models here.
from charity_app.models import Institution, Category, Donation

admin.site.register(Institution)
admin.site.register(Category)
admin.site.register(Donation)