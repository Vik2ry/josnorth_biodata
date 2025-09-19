from django.contrib import admin
from .models import Profile, Event, Resource, Team


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id", "first_name", "last_name", "email", "phone",
        "occupation", "verified", "created_at",
    )
    search_fields = ("first_name", "last_name", "email", "phone", "occupation")
    list_filter = ("verified", "created_at", "ward", "lga")
    readonly_fields = ("created_at",)
    # prepopulated_fields = {"slug": ("first_name", "last_name")}
    fieldsets = (
        ("Basic Info", {
            "fields": ("first_name", "last_name", "slug", "date_of_birth", "occupation")
        }),
        ("Contact", {
            "fields": ("phone", "email", "ward", "lga")
        }),
        ("Profile", {
            "fields": ("photo", "bio", "skills", "education", "experience")
        }),
        ("Verification", {
            "fields": ("verified", "featured_until")
        }),
        ("Metadata", {
            "fields": ("created_at",),
        }),
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "location", "start", "end", "is_public", "created_at")
    search_fields = ("title", "location")
    list_filter = ("is_public", "created_at", "start")
    readonly_fields = ("created_at",)
    # prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Event Details", {
            "fields": ("title", "slug", "description", "location", "start", "end", "cover_image")
        }),
        ("Settings", {
            "fields": ("is_public",),
        }),
        ("Metadata", {
            "fields": ("created_at",),
        }),
    )


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "resource_type", "is_public", "created_at")
    search_fields = ("title", "tags")
    list_filter = ("resource_type", "is_public", "created_at")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Resource", {
            "fields": ("title", "description", "resource_type", "url", "file", "tags")
        }),
        ("Visibility", {
            "fields": ("is_public",),
        }),
        ("Metadata", {
            "fields": ("created_at",),
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name", "description")
    readonly_fields = ("created_at",)
    # prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("members",)  # Better UI for many-to-many
    fieldsets = (
        ("Team Info", {
            "fields": ("name", "slug", "description", "members")
        }),
        ("Metadata", {
            "fields": ("created_at",),
        }),
    )
