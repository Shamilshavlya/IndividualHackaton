from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from main import views
from main.views import *


router = DefaultRouter()
router.register('movie', MovieViewSet)
router.register('category', CategoryViewSet)
router.register('actor', ActorViewSet)
router.register('genre', GenreViewSet)
router.register('review', ReviewViewSet)
router.register('director', DirectorViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/account/', include('account.urls')),
#     path('api-auth/', include('rest_framework.urls')),
#     path('v1/api/', include(router.urls)),
#
# ]


schema_view = get_schema_view(
    openapi.Info(
        title="Movie project API",
        default_version='v1',
        description="This is test movie project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny], )

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    # path('api/v1/review/', views.ReviewDetailView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


