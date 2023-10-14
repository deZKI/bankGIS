from django_filters import rest_framework as django_filters

from .models import BankBranch, ATM

class BankBranchFilter(django_filters.FilterSet):
    """ Фильтр отделения банков """
    service_name = django_filters.CharFilter(field_name='services__name', lookup_expr='exact')

    class Meta:
        model = BankBranch
        fields = ['sale_point_name', 'address', 'service_name']


class ATMFilter(django_filters.FilterSet):
    """ Фильтр банкоматов """
    class Meta:
        model = ATM
        fields = []