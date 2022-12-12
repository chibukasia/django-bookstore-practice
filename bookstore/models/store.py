from django.db import models 
from .book import Book

class Store(models.Model):
    name = models.CharField(max_length=255) 
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name