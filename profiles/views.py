from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profiles
from blog.models import Post  
from blog.forms import PostForm  

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

    if request.method == 'POST':
        # Handle the form submission to create a new post
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('profiles_me')  # Redirect to the home page after post creation
        else:
            messages.error(request, 'Error creating post. Please check the form.')

    else:
        form = PostForm()  # Instantiate an empty form

    return render(
        request,
        "profiles/profiles.html",
        {"profiles": profiles, "form": form},  # Pass the form to the template context
    )

