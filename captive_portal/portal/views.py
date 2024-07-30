# portal/views.py
from django.shortcuts import render
from .models import CaptivePortalContent

def index(request):
    # Get the latest content or create a default one if none exists
    content = CaptivePortalContent.objects.last()
    if not content:
        content = CaptivePortalContent(message="Welcome to KNLS!", image=None)
    return render(request, 'index.html', {'content': content})


# Create your views here.
