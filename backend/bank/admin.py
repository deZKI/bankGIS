from django.contrib import admin

from .models import ATM, ATMService


@admin.register(ATM)
class ATMAdmin(admin.ModelAdmin):
    list_display = ('address', 'latitude', 'longitude', 'allDay')


@admin.register(ATMService)
class ATMServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'capability', 'activity')
