from django.db import models

# Create your models here.
class Demo(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField(max_length=50)
    image1=models.ImageField(blank=True,null=True,upload_to='media/')
    facebook_link=models.CharField(max_length=300,null=True,blank=True)
    insta_link=models.CharField(max_length=300,null=True,blank=True)