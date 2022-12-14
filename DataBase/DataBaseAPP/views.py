from django.shortcuts import render,redirect
from .forms import CreatePostsForm
from .models import Articles



def index(request):
    CreateForm = CreatePostsForm()
    if request.method == "POST":
        CreateForm = CreatePostsForm(request.POST)
        if CreateForm.is_valid():
            name = CreateForm.cleaned_data["name"]
            url = CreateForm.cleaned_data["url"]
            content = CreateForm.cleaned_data["content"]
            published = CreateForm.cleaned_data["published"]
            category = CreateForm.cleaned_data["category"]
            if published == True:
                published = "Опубликовано"
                Articles.objects.create(title=name, url=url, content=content, published=published, category=category)
                return redirect('http://127.0.0.1:8000/news')
    return render(request,"index.html",{"form":CreateForm})

def news(request):
    news=Articles.objects.all()
    return render(request,"news.html",{"news":news})