from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profiles
from blog.forms import PostForm

@login_required
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
    profiles = Profiles.objects.latest('updated_on')

    if request.method == 'POST':
        # Handle the form submission to create a new post
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('home')  # Redirect to home page after post creation
        else:
            # Display specific error messages for each field
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error with {field}: {error}')

    else:
        form = PostForm()  # Instantiate an empty form

    return render(
        request,
        "profiles/profiles.html",
        {"profiles": profiles, "form": form},  # Pass the form to the template context
    )

