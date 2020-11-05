from django.contrib import admin
from .models import Demo
# Register your models here.
class people(admin.ModelAdmin):
    list_display=('name','age','email')


admin.site.register(Demo,people)    