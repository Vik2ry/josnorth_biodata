from rest_framework import serializers
from .models import Profile, Event, Resource, Team

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('slug','created_at')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('slug','created_at')

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
        read_only_fields = ('created_at',)

class TeamSerializer(serializers.ModelSerializer):
    members = ProfileSerializer(many=True, read_only=True)
    members_ids = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), many=True, write_only=True, source='members')
    class Meta:
        model = Team
        fields = '__all__'
