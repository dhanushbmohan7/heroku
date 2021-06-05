from django.shortcuts import render
from .models import Demo,users




                
def index(request):
    all=Demo.objects.all()
    def get_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

            
        return ip

    ip=get_ip(request)
    u=users(user=ip)
    lst=[]
    all_ip=users.objects.all()
    for i in all_ip:
        lst.append(i.user)
    print(lst)    
    
    if ip in lst:
        pass
    else:
        u.save()
    count=users.objects.all().count()



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
