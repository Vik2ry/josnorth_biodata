from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from dj_rest_auth.registration.views import RegisterView
from .models import Profile, Event, Resource, Team
from .serializers import ProfileSerializer, EventSerializer, ResourceSerializer, TeamSerializer
from .permissions import IsAdminOrReadOnly
from .user_serializers import AdminRegistrationSerializer

@extend_schema(
    tags=["Profiles"],   # 👈 groups under Profiles
    description="""
Profiles represent community members’ **biodata**.  
They contain personal, educational, and professional details.

**Public Access:** Anyone can view profiles.  
**Restricted Access:** Only authenticated admins can create, update, or delete profiles.
    """,
    examples=[
        OpenApiExample(
            "Create Profile Example",
            request_only=True,
            value={
                "first_name": "Grace",
                "last_name": "Danladi",
                "date_of_birth": "1992-06-15",
                "occupation": "Software Engineer",
                "phone": "+2348012345678",
                "email": "grace@example.com",
                "ward": "Angwan Rukuba",
                "lga": "Jos North",
                "bio": "Passionate about ICT development and youth empowerment.",
                "skills": ["Python", "Django", "AI/ML"],
                "education": [{"school": "UNIJOS", "degree": "BSc Computer Science"}],
                "experience": [{"role": "Backend Dev", "company": "TechHub"}]
            }
        )
    ]
)
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-featured_until', '-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(
    tags=["Events"],   # 👈 groups under Events
    description="""
Events represent **community gatherings, trainings, and activities**.

**Fields:**  
- title, description, location, start/end datetime  
- optional cover image  

**Public Access:** View events.  
**Restricted Access:** Only admins can create/update/delete.
    """,
    examples=[
        OpenApiExample(
            "Create Event Example",
            request_only=True,
            value={
                "title": "Youth Digital Training",
                "description": "One-week intensive ICT training program.",
                "location": "Jos North Town Hall",
                "start": "2025-10-01T09:00:00Z",
                "end": "2025-10-07T17:00:00Z"
            }
        )
    ]
)
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-start')
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(
    tags=["Resources"],   # 👈 groups under Resources
    description="""
Resources represent **documents, links, or videos** shared with the community.

**Types:** `doc`, `link`, `video`  
- `doc`: File upload (e.g., PDF, Word doc)  
- `link`: External resource link  
- `video`: Video link or file  

**Public Access:** Anyone can view resources marked `is_public=True`.  
**Restricted Access:** Only admins can upload or manage resources.
    """,
    examples=[
        OpenApiExample(
            "Create Document Resource",
            request_only=True,
            value={
                "title": "ICT Roadmap 2025",
                "description": "Strategic plan for ICT in Jos North.",
                "resource_type": "doc",
                "tags": ["strategy", "ict", "planning"]
            }
        ),
        OpenApiExample(
            "Create Link Resource",
            request_only=True,
            value={
                "title": "Community Facebook Page",
                "resource_type": "link",
                "url": "https://facebook.com/josnorthict"
            }
        )
    ]
)
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(is_public=True).order_by('-created_at')
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(
    tags=["Teams"],   # 👈 groups under Teams
    description="""
Teams represent **groups of community members** working together.  

Each team has:  
- name, description  
- list of member profiles  

**Public Access:** Teams and members can be viewed by anyone.  
**Restricted Access:** Only admins can create/update/delete teams or assign members.
    """,
    examples=[
        OpenApiExample(
            "Create Team Example",
            request_only=True,
            value={
                "name": "ICT Volunteers",
                "description": "A team of volunteers driving ICT awareness.",
                "members_ids": [1, 2, 3]
            }
        )
    ]
)
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema(
    tags=["Auth"],
    description="Endpoint for an authenticated admin to create a new admin user. The new user will have `is_staff=True`."
)
class AdminRegistrationView(RegisterView):
    """
    Custom registration view for creating admin users.
    """
    serializer_class = AdminRegistrationSerializer
    permission_classes = [IsAdminUser]
