from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import PostList


def CreatePost(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    posts = PostList.objects.all()
    return render(request, 'news.html', {'postlist': posts})
