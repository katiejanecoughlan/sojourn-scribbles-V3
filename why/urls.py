from django.urls import path
from . import views


urlpatterns = [
    path('', views.why_ss, name='why'),
]