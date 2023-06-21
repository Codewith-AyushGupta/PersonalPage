from django.contrib import admin
from django.urls import path,include
from . import views
import blogs
urlpatterns = [
    path('',views.home,name="home"),

    path('blogs',include('blogs.urls'),
    name="blogs"),

    path('contactus/',include('contactus.urls'),
    name="contactus"),

    path('loogin/',include('blogs.urls'),name="loogin"),

    path('registration/',include('blogs.urls'),name="registration"),

    path('project/<str:id>',views.personal_project_page,name="personal_project_page"),
]
