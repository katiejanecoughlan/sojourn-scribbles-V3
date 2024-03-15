from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import User


@admin.register(User)
class UserAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


