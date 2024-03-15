from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profiles


@admin.register(Profiles)
class UserProfileAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)


