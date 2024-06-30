from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from post.forms import PostForm, CommentForm, CategoryForm
from post.models import Post, Comment, Category


# Create your views here.

def show_posts(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts
    }
    return render(request, 'post/home.html', context=ctx)

def show_category(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories
    }
    return render(request, 'post/category.html', context=ctx)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    ctx = {
        'form': form
    }
    return render(request, 'post/add_post.html',context=ctx)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    ctx = {
        'form': form
    }
    return render(request, 'post/add_category.html', context=ctx)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm(instance=post)
    ctx = {
        'form': form,
        'post': post,
    }
    return render(request, 'post/edit_post.html', context=ctx)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    ctx = {'post': post}
    return render(request, 'post/delete_post.html', context=ctx)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    ctx = {'category': category}
    return render(request, 'post/delete_category.html', context=ctx)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm(instance=category)
    ctx = {
        'form': form,
        'category': category,
    }
    return render(request, 'post/edit_category.html', context=ctx)
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_info', pk=pk)
    else:
        form = CommentForm()
    ctx = {
        'form':form
    }
    return render(request, 'post/add_comment.html', context=ctx)

def post_info(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    ctx = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post/post_info.html', context=ctx)

def category_info(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)
    ctx = {
        'category': category,
        'posts': posts
    }
    return render(request, 'post/category_info.html', context=ctx)



def authors_and_posts(request):
    authors = User.objects.all()
    author_posts = []

    for author in authors:
        posts = Post.objects.filter(comment__author=author)
        author_posts.append({'author': author, 'posts': posts})

    context = {
        'author_posts': author_posts,
    }
    return render(request, 'post/authors_post.html', context)