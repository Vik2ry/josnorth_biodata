from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
import secrets

User = get_user_model()

class Profile(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    ward = models.CharField(max_length=120, blank=True)
    lga = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to='profiles/photos/', blank=True, null=True)
    bio = models.TextField(blank=True)
    skills = ArrayField(models.CharField(max_length=80), default=list, blank=True)
    education = models.JSONField(default=list, blank=True)
    experience = models.JSONField(default=list, blank=True)
    verified = models.BooleanField(default=False)
    featured_until = models.DateTimeField(null=True, blank=True)   # used by background task
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")[:250]
        super().save(*args, **kwargs)

class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='events/covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:250]
        super().save(*args,**kwargs)

class Resource(models.Model):
    RESOURCE_TYPES = (('doc','Document'), ('link','Link'), ('video','Video'))
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, default='doc')
    url = models.URLField(blank=True)
    file = models.FileField(upload_to='resources/files/', blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=80), default=list, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(Profile, blank=True, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
