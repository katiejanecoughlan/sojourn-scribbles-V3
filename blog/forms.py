from django import forms
from django_countries.fields import CountryField
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    """
    Form class for users to create a post
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'country', 'featured_image','content', 'excerpt', 'status',)
