from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Profiles
from .forms import ProfileForm
from blog.forms import PostForm


@login_required
def profiles_me(request):
    profiles_queryset = Profiles.objects.filter(user=request.user)
    if profiles_queryset.exists():
        profile = profiles_queryset.first()
    else:
        profile = None

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=profile)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()  # This will automatically handle the featured_image upload to Cloudinary
            messages.success(request, 'Post created successfully.')
            return redirect('home')

        elif profile_form.is_valid():
            profile_instance = profile_form.save(commit=False)
            profile_instance.user = request.user
            profile_instance.save()
            # messages.success(request, 'Profile updated successfully.')  # Disabled due to bug

            # Fetch the updated profile instance
            updated_profile = Profiles.objects.get(pk=profile_instance.pk)

            return render(request, "profiles/profiles.html",
                          {"profile_form": profile_form,
                           "post_form": post_form,
                           "profiles": updated_profile})

        else:
            # If neither form is valid, show an error message
            messages.error(request, 'Error creating post or updating profile.')
    else:
        # If not a POST request, initialize forms without any submitted data
        post_form = PostForm()
        profile_form = ProfileForm(instance=profile)

    return render(request, "profiles/profiles.html",
                  {"profile_form": profile_form,
                   "post_form": post_form, "profiles": profile})
