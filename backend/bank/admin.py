from django.contrib import admin

from .models import ATM, ATMService, BankBranch, UserComment, Workload


class UserCommentTabular(admin.TabularInline):
    model = UserComment


class WorkloadTabular(admin.TabularInline):
    model = Workload


@admin.register(ATM)
class ATMAdmin(admin.ModelAdmin):
    list_display = ('address', 'latitude', 'longitude', 'allDay')


@admin.register(ATMService)
class ATMServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'capability', 'activity')


@admin.register(BankBranch)
class BankBranchAdmin(admin.ModelAdmin):
    list_display = ('sale_point_name', 'address', 'status')
    inlines = [UserCommentTabular, WorkloadTabular]


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('branch', 'author', 'stars')
