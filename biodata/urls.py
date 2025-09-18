from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, EventViewSet, ResourceViewSet, TeamViewSet

router = DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('events', EventViewSet)
router.register('resources', ResourceViewSet)
router.register('teams', TeamViewSet)

urlpatterns = [path('', include(router.urls))]
