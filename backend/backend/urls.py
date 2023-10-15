from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from bank.views import download_atm, download_bankBranch, match_service, BankBranchViewSet, ATMViewSet

router = DefaultRouter()
router.register(r'bank-branches', BankBranchViewSet)
router.register(r'bank-atm', ATMViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="bankGIS API",
        default_version='v1',
        description="АPI для хакатона MoreTech5.0",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/download_atm', download_atm),
    path('api/download_bankBranch', download_bankBranch),
    path('api/match_service', match_service),
    path('api/', include(router.urls)),

    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
