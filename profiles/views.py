from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profiles
from .forms import ProfileForm
from blog.forms import PostForm

@login_required
def profiles_me(request):
    profiles = Profiles.objects.filter(user=request.user).first()  # Use filter() instead of get()

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()  # This will automatically handle the featured_image upload to Cloudinary
            messages.success(request, 'Post created successfully.')
            return redirect('home')
        elif profile_form.is_valid():
            # Process profile_form data
            profile_instance = profile_form.save(commit=False)
            profile_instance.user = request.user
            profile_instance.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profiles_me')
        else:
            messages.error(request, 'Error creating post.')
    else:
        post_form = PostForm()
        profile_form = ProfileForm()

    return render(request, "profiles/profiles.html", {"profiles": profiles, "post_form": post_form, "profile_form": profile_form})


