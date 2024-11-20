from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from seller.views import notifications_view


schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('admin/', admin.site.urls),
    path('notifications/', notifications_view, name='notifications'),
]
