

# Register your models here.
from django.contrib import admin
from .models import BankCoordinates, Bank, BankBranch, IndividualATM

@admin.register(BankCoordinates)
class BankCoordinatesAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'latitude', 'longitude')

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BankBranch)
class BankBranchAdmin(admin.ModelAdmin):
    list_display = ('bank', 'coordinates')
    raw_id_fields = ('bank', 'coordinates')

@admin.register(IndividualATM)
class IndividualATMAdmin(admin.ModelAdmin):
    list_display = ('bank', 'coordinates')
    raw_id_fields = ('bank', 'coordinates')