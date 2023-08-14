from django.contrib import admin
from .models import BloodDonate , Donor
# Register your models here.
# admin.site.register(BloodDonate)
# admin.site.register(Donor)


@admin.register(BloodDonate)
class BloodDonateAdmin(admin.ModelAdmin):
    list_display = ['donor'  , 'date' , 'unit', 'bloodgroup']

@admin.register(Donor)
class BloodDonorAdmin(admin.ModelAdmin):
    list_display = ['user'  , 'mobile' , 'bloodgroup']