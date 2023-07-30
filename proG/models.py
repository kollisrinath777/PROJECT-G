from django.db import models




# Create your models here.

class Profriends(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    acres=models.CharField(max_length=100)
    dest=models.CharField(max_length=100)


class ProGandlavedu:
    name: str
    desc:str
    members:int
    age:str
    dest:str
