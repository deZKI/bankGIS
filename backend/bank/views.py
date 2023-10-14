import json

from django.http import HttpResponse

from .models import ATM, ATMService


def download_atm(request):
    with open('./vtb_data/atms.txt', 'r') as file:
        ATM.objects.all().delete()
        data = json.loads(file.read())
        added_atm = 0
        for atm_data in data["atms"]:
            if ATM.objects.filter(
                    address=atm_data["address"],
                    latitude=atm_data["latitude"],
                    longitude=atm_data["longitude"],
                    allDay=atm_data["allDay"]
            ).exists():
                continue

            atm, existed = ATM.objects.get_or_create(
                address=atm_data["address"],
                latitude=atm_data["latitude"],
                longitude=atm_data["longitude"],
                allDay=atm_data["allDay"]
            )
            if not existed:
                for service_name, service_data in atm_data["services"].items():
                    capability = service_data["serviceCapability"]
                    activity = service_data["serviceActivity"]
                    # Создание и связывание экземпляров ATMService с банкоматом и услугой
                    service = ATMService.objects.get_or_create(name=service_name, capability=capability,
                                                               activity=activity)[0]
                    atm.services.add(service)
                added_atm += 1

    return HttpResponse(f'Добавлено объектов {added_atm}')
