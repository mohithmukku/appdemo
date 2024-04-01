from django.db import models

from datetime import datetime
from django.utils import timezone
timezone.now()

# Create your models here.

#this model class is for to upload our database content in template or html page and open in own broser
class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now)
    #images...
    image=models.ImageField(upload_to="images/")
    #videos...
    video=models.FileField(upload_to="media/")
    def __str__(self):
        return self.title 
    
#this model class is for uploading or storing the details given in webpage to database and again displaying details in web page also
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    #message=models.TimeField()
    image=models.ImageField(upload_to="images/")
    created_at=models.DateTimeField(default=datetime.now)
    is_resolved=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
#this model class is for uploading or storing the details given in webpage to database and again displaying details in web page also
class MarksForm(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.IntegerField()
    section=models.CharField(max_length=50)
    marks=models.IntegerField()
    created_at=models.DateTimeField(default=datetime.now)
    is_resolved=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

"""   class AddBooks(models.Model):
        author=models.CharField(max_length=200,null=False,blank=False)
        title=models.CharField(max_length=200,null=False,blank=False)
        description=models.TextField()

        def __str__(self):
            return self.title       """