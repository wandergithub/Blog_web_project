from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm 
from django.contrib.auth.decorators import login_required


def home(request):
    """Render the Home page, Showing all the posts"""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts':posts}
    return render(request, 'Blogs/home.html', context)

@login_required
def new_post(request):
    """Adds a new post."""
    if request.method != "POST":
        # No data submitted; create a new form
        form = BlogForm()
    else:
        # Post data submitted; porcess data.
        form = BlogForm(data = request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('Blogs:home')
    # Display a blank or invalid form.
    context = {'form':form}
    return render(request,'Blogs/new_post.html',context)

@login_required
def edit_post(request, post_id):
    """ Edit existing posts."""
    post = BlogPost.objects.get(id = post_id)
    check_if_user_owns_data(request, post)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current post.
        form = BlogForm(instance = post)
    else:
        # POST data submitted; process data.
        form = BlogForm(instance = post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blogs:home')
    
    context = {'post':post,'form':form}
    return render(request, 'Blogs/edit_post.html', context)

def check_if_user_owns_data(request, post):
    """ Evaluates if the owner of the post matches the current user."""
    if post.owner != request.user:
        raise Http404