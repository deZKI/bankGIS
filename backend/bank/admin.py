from django.contrib import admin
from django_admin_inline_paginator.admin import TabularInlinePaginated

from .models import ATM, ATMService, BankBranch, UserComment, Workload, BranchService


class UserCommentTabular(TabularInlinePaginated):
    model = UserComment
    per_page = 5

class WorkloadTabular(TabularInlinePaginated):
    model = Workload
    per_page = 5

@admin.register(BranchService)
class BranchServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)

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
    list_filter = ('services', )


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('branch', 'author', 'stars')
