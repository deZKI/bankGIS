from django.shortcuts import render

from map.models import BankCoordinates
from faker import Faker
from .models import Bank, BankBranch, IndividualATM, BankCoordinates



def index(request):
    # create_random_data()
    stations = list(BankCoordinates.objects.values("latitude","longitude" )[:100])
    ATM=IndividualATM.objects.all()
    # banks = list(Bank.objects.values('name'))

    print(stations)
    return render(request, 'index.html', {'stations': stations,"ATM":ATM})
import random
from faker import Faker

def create_random_data():
    fake = Faker()

    # Создаем запись для банка ВТБ
    coordinate = BankCoordinates(station_name = "vtb",latitude=55.751244, longitude=37.618423)
    coordinate.save()

    bank = Bank(name="VTB", coordinates=coordinate)
    bank.save()


    # Генерируем данные филиалов и банкоматов в Москве
    # Подразумевая, что географические координаты находятся в пределах Москвы
    for _ in range(20):

        # Создаем случайные координаты в Москве
        station_name = f"Хабаровск, {fake.street_address()}"
        latitude = float(f"{48}.{random.randint(100000, 999999)}")
        longitude = float(f"{135}.{random.randint(100000, 999999)}")
        bank_coords = BankCoordinates(station_name=station_name, latitude=latitude, longitude=longitude)
        bank_coords.save()

        # Создаем филиал ВТБ с этими координатами
        branch = BankBranch(bank=bank, coordinates=bank_coords)
        branch.save()

        # Создаем банкомат ВТБ с этими координатами
        atm = IndividualATM(bank=bank, coordinates=bank_coords)
        atm.save()

