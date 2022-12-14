from django.contrib import admin
from django.urls import path
from DataBaseAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('news', views.news),

]



