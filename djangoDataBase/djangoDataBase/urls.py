from django.contrib import admin
from django.urls import path
from djangoDataBaseAPP import views

urlpatterns = [
    path('createPost', views.CreatePost),
    path('admin/', admin.site.urls),
    path('news', views.index, name='news')
]
