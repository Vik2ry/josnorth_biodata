from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, EventViewSet, ResourceViewSet, TeamViewSet, AdminRegistrationView

router = DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('events', EventViewSet)
router.register('resources', ResourceViewSet)
router.register('teams', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/admin/', AdminRegistrationView.as_view(), name='admin_register'),
]
