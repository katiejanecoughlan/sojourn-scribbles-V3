from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profiles
from blog.forms import PostForm

@login_required
def profiles_me(request):
    profiles = Profiles.objects.latest('updated_on')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()  # This will automatically handle the featured_image upload to Cloudinary
            messages.success(request, 'Post created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Error creating post.')
    else:
        form = PostForm()

    return render(request, "profiles/profiles.html", {"profiles": profiles, "form": form})
