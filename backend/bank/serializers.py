from rest_framework.serializers import ModelSerializer

from .models import BranchService


class BranchServiceSerializer(ModelSerializer):
    """ Типы услуг отделы банка"""

    class Meta:
        model = BranchService
        fields = ('name',)
