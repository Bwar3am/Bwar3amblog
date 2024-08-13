from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100 , null=True)
    time_created = models.TimeField(auto_now=True , null=False)
    description = models.CharField(max_length=250 ,null=True)
    body = models.CharField(max_length=10000 , null=False)
    image = models.ImageField(upload_to='pics/' , default="pics/placeholder.png" , null=True)
    date = models.DateField(null=False , default=datetime.now)
    
    def __str__(self):
        return  self.title
    
    @property
    def imageURL(self):
            try:
                url = self.image.url
            except:
                url = ''
            return url