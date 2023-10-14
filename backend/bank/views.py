import json

from django.http import HttpResponse

from .models import ATM, ATMService, BankBranch, OpeningHours, UserComment, Workload


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


def download_bankBranch(request):
    with open('./vtb_data/merged.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for branch_data in data:
        branch = BankBranch.objects.create(
            sale_point_name=branch_data["salePointName"],
            address=branch_data["address"],
            status=branch_data["status"],
            rko=branch_data["rko"],
            office_type=branch_data["officeType"],
            sale_point_format=branch_data["salePointFormat"],
            suo_availability=branch_data["suoAvailability"],
            has_ramp=branch_data["hasRamp"],
            latitude=branch_data["latitude"],
            longitude=branch_data["longitude"],
            metro_station=branch_data["metroStation"],
            distance=branch_data["distance"],
            kep=branch_data["kep"],
            my_branch=branch_data["myBranch"],
            review_count=branch_data["review_count"],
            estimation=branch_data["estimation"]
        )

        # Сохранение данных о часах работы
        for hours_data in branch_data["openHours"]:
            time, exits = OpeningHours.objects.get_or_create(days=hours_data["days"],
                                                             hours=hours_data["hours"])
            branch.open_hours.add(time)

        for hours_data in branch_data["openHoursIndividual"]:
            time, exits = OpeningHours.objects.get_or_create(days=hours_data["days"],
                                                             hours=hours_data["hours"])
            branch.open_hours_individual.add(time)

        for day, day_data in branch_data['time'].items():
            for hour_data in day_data:
                hour, people_count = hour_data
                Workload.objects.create(day=day, hour=hour, people_count=people_count, branch=branch)

        # Сохранение данных об отзывах
        user_comments_data = branch_data["user_comments"]
        for author, comment_data in user_comments_data.items():
            UserComment.objects.create(branch=branch, author=author, stars=comment_data["stars"],
                                       text=comment_data["text"])
    return HttpResponse(f'Добавлено оьъектов')
