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

def profile(request,id):
    person=Demo.objects.get(id=id)

    return render(request,'profile.html',{'name':person.name,'age':person.age,'pic':person.image1})    

def search(request):
    if request.method == 'GET':
        name=request.GET.get('search')
        person=Demo.objects.get(name=name)
        print('person name:',person.name)

    return render(request,'profile.html',{'name':person.name,'age':person.age,'pic':person.image1})        