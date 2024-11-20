from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from seller.views import notifications_view
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, ProductViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
    ),
    public=True,
)


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('notifications/', notifications_view, name='notifications'),
]
