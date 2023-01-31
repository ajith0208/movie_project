from django.shortcuts import render, redirect

from .form import Movieform
from .models import movie_list


# Create your views here.

def index(request):
    movies = movie_list.objects.all()
    return render(request, 'index.html', {'movies': movies})


def details(request, movie_id):
    movie = movie_list.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    length = len(movie_list.objects.all())
    if request.method == 'POST':
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        director = request.POST.get('director', )
        img = request.FILES.get('img', )
        movie = movie_list(id=length + 1, name=name, year=year, director=director, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, movie_id):
    movie = movie_list.objects.get(id=movie_id)
    form = Movieform(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})


def delete(request, movie_id):
    if request.method == 'POST':
        movie = movie_list.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html', {'movie': movie_list.objects.get(id=movie_id)})
