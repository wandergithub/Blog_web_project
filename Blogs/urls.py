"""Defining urls patterns for Blogs app."""
from django.urls import path
from . import views

app_name = 'Blogs'

urlpatterns = [
    #homepage
    path('',views.home, name = 'home'),
    # New post page
    path('new_post',views.new_post, name = 'new_post'),
    # Edit post
    path('edit_post/<int:post_id>/',views.edit_post, name= 'edit_post'),
]