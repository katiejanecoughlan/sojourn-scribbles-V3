from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django_countries import countries as django_countries_list
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(status=1)
        author_id = self.request.GET.get('user')
        country_code = self.request.GET.get('country')  # Get selected country code
        if author_id:
            queryset = queryset.filter(author__id=author_id)
        if country_code:  # Check if country filter is applied
            queryset = queryset.filter(country__iexact=country_code)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filter users who have authored posts
        context['users'] = User.objects.filter(blog_posts__isnull=False).distinct()
        # Get all distinct country codes selected in blog posts
        selected_country_codes = Post.objects.values_list('country', flat=True).distinct()
        # Get country names corresponding to the selected country codes
        selected_countries = [country for country in django_countries_list if country[0] in selected_country_codes]
        # Pass the selected countries to the template
        context['countries'] = selected_countries
        # Pass the selected country code to the template
        context['selected_country'] = self.request.GET.get('country')
        return context



def post_detail(request, slug):
    """
    Retrieves a specific post by slug and displays its details.

    **Context**

    ``post``
        The retrieved :model:`blog.Post` object.
    ``comments``
        All comments associated with the post.
    ``comment_count``
        Total count of approved comments for the post.
    ``comment_form``
        Form instance for submitting new comments.

    ``users``
        All registered users in the system.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Fetch all users
    users = User.objects.all()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "users": users,  # Pass the users queryset to the context
        },
    )

@login_required
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # Check if the current user is the author of the post
    if request.user == post.author:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    else:
        messages.error(request, 'You can only delete your own posts!')
    
    return HttpResponseRedirect(reverse('home'))  # Redirect to the post list page after deletion
