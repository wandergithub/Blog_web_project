from typing import Text
from django.db import models
from django.urls.converters import StringConverter
from django.contrib.auth.models import User

class BlogPost(models.Model):
    Title = models.CharField(max_length = 40) 
    Text = models.CharField(max_length = 1000)
    date_added = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.Title
