from django.contrib import admin
from .models import Demo,users
# Register your models here.
class people(admin.ModelAdmin):
    list_display=('name','age','email','image1')
class USERS(admin.ModelAdmin):
    list_display=['user']    


admin.site.register(Demo,people)    
admin.site.register(users,USERS)
