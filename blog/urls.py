from django.urls import path
from . import views
from .views import post_delete

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/delete/', post_delete, name='post_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
