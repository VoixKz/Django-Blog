from django.shortcuts import render, redirect
from .models import Genre, Post


def post_list(request):
    genre_id = request.GET.get('genre_id')
    if genre_id:
        posts = Post.objects.filter(genre__id=genre_id)
    else:
        posts = Post.objects.all()
    
    genres = Genre.objects.all()
    context = {
        'posts': posts, 
        'genres': genres
    }
    return render(request, 'djangoPosts/post_list.html', context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'djangoPosts/post.html', context)


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        genre = Genre.objects.get(id = request.POST.get('genre'))
        if 'image' in request.FILES:
            image = request.FILES['image']
            image.name = f"media/images/{image.name}"
        else:
            image = None
        Post.objects.create(title=title, content=content, genre=genre, image=image)
        return redirect('post_list')
    
    genres = Genre.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'djangoPosts/post_create.html', context)