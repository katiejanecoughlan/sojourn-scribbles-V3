from django.shortcuts import render
from django.contrib import messages
from .models import Profiles


def profiles_me(request):
    """
    Renders the most recent information on the website author.

    Displays an individual instance of :model:`profiles.Profiles`.

    **Context**
    ``profiles``
        The most recent instance of :model:`profiles.Profiles`.
        
    **Template**
    :template:`profiles/profiles.html`
    """
    profiles = Profiles.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "profiles/profiles.html",
        {"profiles": profiles},
    )
