# from typing_extensions import Required
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from tinymce import models  as tinymce_models
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class blogs_database(models.Model):
    unique_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    links = models.CharField(default="",max_length=500,blank=True)
    blog_type=models.CharField(default="",max_length=500)
    status = models.IntegerField(choices=STATUS, default=1)
    message=tinymce_models.HTMLField()
    updated_on = models.DateTimeField(auto_now=True)
    image=models.ImageField()
    date_time=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title

class loogin_data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100 ,default="abc@gmail.com")
    phone=models.IntegerField()
    Date_of_birth= models.DateField()
    def __str__(self):
        return self.name

class BlogComments(models.Model):
    sno=models.AutoField(primary_key=True)
    comments=models.TextField()
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    post=models.ForeignKey(blogs_database,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=datetime.now())
    def __str__(self):
            return self.user

class project(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    short_about = tinymce_models.HTMLField()
    Project_url = models.CharField(default="",max_length=500)
    decription=tinymce_models.HTMLField()
    image=models.ImageField()
    status = models.IntegerField(choices=STATUS, default=1)
    date_time=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title