from django.shortcuts import render
from .models import Demo
# Create your views here.
def index(request):
    all=Demo.objects.all()


    return render(request,'index.html',{'all':all})

def second(request):
    return render(request,'second.html')  

def photos(request):
    pics=Demo.objects.only('image1')
    
    return render(request,'photos.html',{'pics':pics})      