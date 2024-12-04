from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from backend import views

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation with Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'endereco', views.EnderecoViewSet)
router.register(r'servico', views.ServicoViewSet)
router.register(r'formapagamento', views.FormaPagamentoViewSet)
router.register(r'ordemservico', views.OrdemServicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eletricista/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]