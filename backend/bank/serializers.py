from rest_framework.serializers import ModelSerializer

from .models import BranchService, BankBranch, OpeningHours


class BranchServiceSerializer(ModelSerializer):
    """ Типы услуг отделы банка"""

    class Meta:
        model = BranchService
        fields = ('name',)

class OpeningHoursSerializer(ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'

class BankBranchSerializer(ModelSerializer):
    """ Сериализатор на отделения банков"""
    services = BranchServiceSerializer(many=True)
    open_hours = OpeningHoursSerializer(many=True)
    open_hours_individual = OpeningHoursSerializer(many=True)

    class Meta:
        model = BankBranch
        fields = '__all__'