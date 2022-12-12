from django.db import models 
from .author import Author
from .publisher import Publisher

class Book(models.Model):
    name = models.CharField(max_length=255)
    pages = models.IntegerField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pub_date = models.DateField() 


    def __str__(self):
        return self.name