from django.urls import path,include
from django.contrib import admin
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('admin/',admin.site.urls),
    path('api/v1/',include('biodata.urls')),
    # API schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # ReDoc UI
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
