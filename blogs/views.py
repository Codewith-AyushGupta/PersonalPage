import email
from email import message
from django.shortcuts import render
from django.urls import is_valid_path
from requests import Request
from .models import blogs_database
from .models import loogin_data
from .models import BlogComments
from .models import project
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, redirect
import bs4
# Create your views here.


def home(request):

    data=project.objects.filter(status=1)
    param={"data":data}
    return render(request,'blogs/index.html',param)

def blogs(request):
    # print(bool(User.is_authenticated))
    #if request.user.is_authenticated:
        data=blogs_database.objects.filter(status=1)  ##fetching Data From Database
        comments=BlogComments.objects.filter(post=data)  ##fetching comments Data From Database
        params={"data1":data,'comments':comments}
        return render(request,'blogs/blogs.html',params) #rendering  Fetchded data into html
   # else:
     #   messages.warning(request,"Dont Be x Smart first loogin your self")
      #  return redirect('home')

def personal_project_page(request,id):
    data=project.objects.filter(id=id)
    params={"data":data}
    return render(request,'blogs/personal_project_page.html',params)
def loogin(request):
    if request.method=="POST":
        name=request.POST.get('name') #fetching data from html templates
        password=request.POST.get('pasword') #fetching data from html templates
        print(name,"  ",password)
        # form = AuthenticationForm(request, data=request.POST)
        # print(bs4.BeautifulSoup.prettify(form))
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"{name} You are now logged in.")
            return redirect("home")
        else:
            print("Invalid Credentials")
            messages.error(request,"enter a valid credentials")
            return redirect('loogin')

    return render(request,'blogs/loogin.html')

def registration(request):
    if request.method=="POST":
        print("Hello")
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        DOB=request.POST.get('DOB')
        pass1=request.POST.get('pass1') 
        print(type(pass1),pass1)
        pass2=request.POST.get('pass2')
        if(pass1!=pass2):
            messages.warning(request,"Password Doesnot match")
            return redirect('registration')
        if(len(str(number))!=10):
            messages.warning(request,"Enter a Valid Mobile Number")
            return redirect('registration')
        if(pass1==pass2):
            try:
                myuser=User.objects.create_user(first_name,email,pass2)
                myuser.first_name=first_name
                myuser.last_name=last_name
                myuser.email=email
                myuser.DOB=DOB
                data = loogin_data(name=str(first_name+last_name) , phone=number , email=email , Date_of_birth=DOB)
                data.save()
                myuser.save()
            except:
                messages.warning(request,"try to choose a Unique username")
                return redirect('registration')
            messages.success(request,f"congo {first_name} {last_name} you are sucessfully registred with Database")
            return redirect('loogin')      
    return render(request,'blogs/registration.html')



def logout_view(request):
    logout(request)
    return redirect('loogin')
def user_personal_page(request,unique_id):
    data=blogs_database.objects.filter(unique_id=unique_id)
    params={'data':data}
    return render(request,'blogs/user_personal_page.html',params)

# def postcomment(request):
#     if request.method=="POST":
#         comments=request.post.get('comment')
#         user=request.user
#         postsno=request.post.get(postsno)
#         post=request.post.get(sno=postsno)

#         comment=BlogComments(comments=comments,user=user,post=post)
#         comment.save()
#         messages.warning(request,"comment Added Sucessfullly")
#         return redirect(f"blogs/{user_personal_page.unique_id}")

#     return redirect('home')