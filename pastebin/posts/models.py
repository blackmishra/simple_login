from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class User(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title