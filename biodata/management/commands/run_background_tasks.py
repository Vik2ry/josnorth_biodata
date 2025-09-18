from django.core.management.base import BaseCommand
from django.utils import timezone
from biodata.models import Profile, Event
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Run periodic background tasks: expire featured flags, compute counts."

    def handle(self, *args, **options):
        now = timezone.now()
        # expire featured profiles
        expired = Profile.objects.filter(featured_until__lt=now)
        count_expired = expired.update(featured_until=None)
        self.stdout.write(self.style.SUCCESS(f'Expired {count_expired} featured profiles.'))

        # compute counts
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        upcoming = Event.objects.filter(start__gte=today_start).count()
        new_profiles = Profile.objects.filter(created_at__gte=today_start).count()
        self.stdout.write(self.style.SUCCESS(f'Upcoming events: {upcoming}, New profiles today: {new_profiles}'))

        # (Optional) call external monitoring or Supabase functions here
        logger.info(f'Background run at {now.isoformat()}: upcoming_events={upcoming}, new_profiles_today={new_profiles}')
