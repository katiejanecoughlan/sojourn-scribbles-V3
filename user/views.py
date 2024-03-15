from django.shortcuts import render
from .models import User


def user_me(request):
    """
    Renders the User page
    """
    user = User.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "user/user.html",
        {"user": user},
    )
