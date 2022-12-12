from django.db import models 
from datetime import date
from .blog import Blog
from .author import Author 

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField() 
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline