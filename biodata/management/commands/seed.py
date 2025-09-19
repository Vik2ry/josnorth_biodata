# biodata/management/commands/seed.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from biodata.models import Profile, Event, Resource, Team
import datetime


class Command(BaseCommand):
    help = "Seed the database with demo data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # --- Profiles ---
        john = Profile.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=datetime.date(1990, 5, 21),
            occupation="Software Engineer",
            phone="+2348000000001",
            email="john@example.com",
            ward="Tudun Wada",
            lga="Jos North",
            bio="Passionate about open source and community development.",
            skills=["Python", "Django", "React"],
            education=[{"degree": "BSc Computer Science", "institution": "Unijos", "year": 2013}],
            experience=[{"title": "Backend Developer", "company": "TechCorp", "years": "2014-2018"}],
            verified=True,
        )

        jane = Profile.objects.create(
            first_name="Jane",
            last_name="Smith",
            date_of_birth=datetime.date(1992, 7, 15),
            occupation="Community Organizer",
            phone="+2348000000002",
            email="jane@example.com",
            ward="Angwan Rogo",
            lga="Jos North",
            bio="Organizer for tech events and youth empowerment.",
            skills=["Leadership", "Public Speaking", "Project Management"],
            education=[{"degree": "MBA", "institution": "ABU Zaria", "year": 2018}],
            experience=[{"title": "Community Lead", "company": "Local NGO", "years": "2019-Present"}],
            verified=False,
        )

        # --- Events ---
        event1 = Event.objects.create(
            title="Jos North ICT Summit",
            description="Annual ICT summit bringing together professionals and students.",
            location="Jos City Hall",
            start=timezone.now() + datetime.timedelta(days=10),
            end=timezone.now() + datetime.timedelta(days=11),
            is_public=True,
        )

        event2 = Event.objects.create(
            title="Youth Empowerment Workshop",
            description="A hands-on workshop on digital skills.",
            location="NYSC Secretariat Jos",
            start=timezone.now() + datetime.timedelta(days=30),
            is_public=True,
        )

        # --- Resources ---
        res1 = Resource.objects.create(
            title="Community Guidebook",
            description="A PDF guide for community engagement.",
            resource_type="doc",
            url="",
            tags=["guide", "community"],
            is_public=True,
        )

        res2 = Resource.objects.create(
            title="Official Website",
            description="Main community website link.",
            resource_type="link",
            url="https://josnorthictcds.vercel.app/",
            tags=["website", "info"],
            is_public=True,
        )

        # --- Teams ---
        team1 = Team.objects.create(
            name="Organizers",
            description="Team responsible for planning and coordination."
        )
        team1.members.add(john, jane)

        team2 = Team.objects.create(
            name="Volunteers",
            description="Community volunteers supporting events."
        )
        team2.members.add(jane)

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))
