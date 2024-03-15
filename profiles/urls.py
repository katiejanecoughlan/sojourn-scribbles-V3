from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles_me, name='profiles'),
]