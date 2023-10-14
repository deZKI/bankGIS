import http
import json

from django.http import HttpResponse
from django.db.models import Q, F, FloatField, ExpressionWrapper, Value
from django.db.models.functions import Radians, Cos, Sin, Sqrt, Cast

from django_filters import rest_framework as django_filters

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, filters

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ai import fuzzy_match

from .models import ATM, ATMService, BankBranch, OpeningHours, UserComment, Workload, BranchService
from .serializers import BranchServiceSerializer, BankBranchSerializer
from .filters import BankBranchFilter
from .paginator import CustomPagination
from .utils import haversine_distance, parse_coordinate, Atan2Func


@swagger_auto_schema(
    method='GET',
    operation_summary='Download ATM Data',
    operation_description='Загрузить данные с json базы АТМ',
    responses={
        200: openapi.Response('Successful'),
    },
)
@api_view(['GET'])
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

            atm, created = ATM.objects.get_or_create(
                address=atm_data["address"],
                latitude=atm_data["latitude"],
                longitude=atm_data["longitude"],
                allDay=atm_data["allDay"]
            )
            if created:
                for service_name, service_data in atm_data["services"].items():
                    capability = service_data["serviceCapability"]
                    activity = service_data["serviceActivity"]
                    # Создание и связывание экземпляров ATMService с банкоматом и услугой
                    service = ATMService.objects.get_or_create(name=service_name, capability=capability,
                                                               activity=activity)[0]
                    atm.services.add(service)
                added_atm += 1

    return HttpResponse(f'Добавлено объектов {added_atm}')


@swagger_auto_schema(
    method='GET',
    operation_summary='Download BankBranch Data',
    operation_description='Загрузить данные с json базы Отделений',
    responses={
        200: openapi.Response('Successful'),
    },
)
@api_view(['GET'])
def download_bankBranch(request):
    with open('./vtb_data/baza21.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    branch_count = 0
    for branch_data in data:
        try:
            branch, created = BankBranch.objects.get_or_create(
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

            if not created:
                continue
            branch_count += 1

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

        except Exception as error:
            continue

    return HttpResponse(f'Добавлено оьъектов {branch_count}')


@swagger_auto_schema(
    method='POST',
    operation_summary='Найти услуги по сырому запросу пользователя',
    operation_description='Сервер отдает похожие типы услуг по запросу пользователя',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'query': openapi.Schema(type=openapi.TYPE_STRING, description='Запрос пользователя'),
        },
        required=['query'],
    ),
    responses={
        status.HTTP_200_OK: BranchServiceSerializer(many=True),
        status.HTTP_204_NO_CONTENT: 'Данных нет'
    },
)
@api_view(['POST'])
def match_service(request):
    query = request.data.get('query')
    coincidence = 60

    if query:
        fuzzy_services = fuzzy_match(query, list(BranchService.objects.all().values_list('name', flat=True)))

        services = [service[0] for service in fuzzy_services if service[1] > coincidence]

        matching_services = BranchService.objects.filter(name__in=services)

        serialized_data = BranchServiceSerializer(matching_services, many=True)

        if not serialized_data.data:
            return Response(data='Данных нет')
        return Response(data=serialized_data.data)

    return Response(data='Данных нет')


class BankBranchViewSet(viewsets.ReadOnlyModelViewSet):
    """ VIEW Для отделений банков """
    queryset = BankBranch.objects.all()
    serializer_class = BankBranchSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = BankBranchFilter
    search_fields = ['sale_point_name', 'address', 'services__name']
    ordering_fields = ['sale_point_name', 'address']
    pagination_class = CustomPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'latitude', in_=openapi.IN_QUERY,
                type=openapi.FORMAT_DECIMAL,
                description='Долгота пользователя',
                required=False,
            ),
            openapi.Parameter(
                'longitude', in_=openapi.IN_QUERY,
                type=openapi.FORMAT_DECIMAL,
                description='Широта пользователя',
                required=False,
            )
        ],
        operation_description='Provide either latitude or longitude (or both) to search for bank branches.'
    )
    def list(self, request, *args, **kwargs):
        search_query = request.GET.get('search', '')
        if search_query:
            self.queryset = self.queryset.filter(
                Q(sale_point_name__icontains=search_query) |
                Q(address__icontains=search_query)
            )
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        user_latitude = parse_coordinate(self.request.query_params.get('latitude'))
        user_longitude = parse_coordinate(self.request.query_params.get('longitude'))

        if user_latitude is not None and user_longitude is not None:
            # Переводим в радианы
            user_latitude_rad = Radians(user_latitude)
            user_longitude_rad = Radians(user_longitude)

            queryset = queryset.annotate(
                lat_diff=Radians(Cast(F('latitude'), FloatField())) - user_latitude_rad,
                lon_diff=Radians(Cast(F('longitude'), FloatField())) - user_longitude_rad,
                a=Sin(F('lat_diff') / 2) * Sin(F('lat_diff') / 2) +
                  Cos(user_latitude_rad) * Cos(Radians(Cast(F('latitude'), FloatField()))) *
                  Sin(F('lon_diff') / 2) * Sin(F('lon_diff') / 2),
            ).annotate(
                distance_between_user=ExpressionWrapper(
                    6371 * 2 * Atan2Func(
                        Sqrt(F('a')),
                        Sqrt(1 - F('a'))
                    ),
                    output_field=FloatField()
                )
            ).order_by('distance_between_user')

        return queryset
