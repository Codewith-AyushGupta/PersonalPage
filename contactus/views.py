from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import contact
from django.contrib import messages
#front Python part()
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        phone=request.POST.get('phone')
        data=contact(name=name,email=email,phone=phone,message=message)
        data.save()
        messages.warning(request,"Message Send Sucessfully to Ayush Gupta")
        return redirect('home')
    return render(request,'contactus/contactus.html')

