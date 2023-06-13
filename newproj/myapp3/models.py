from django.db import models
from datetime import datetime

# Create your models here.
class Features(models.Model):
    MainTitle = models.CharField(max_length=20,default="")
    datecreated= models.DateTimeField(default=datetime.now,blank=True)
    body=models.CharField(max_length=200,default="")