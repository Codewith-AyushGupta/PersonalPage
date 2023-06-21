from django.shortcuts import render
from django.http import HttpResponse
from . models import project
# Create your views here.

#front Python part()
def home(request):
    data=project.objects.filter(status=1)
    param={"data":data}
    return render(request,'home/home.html',param)

def personal_project_page(request,id):
    data=project.objects.filter(id=id)
    params={"data":data}
    return render(request,'home/personal_project_page.html',params)