from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField('book title',max_length=255) 
    author = models.CharField('book author',max_length=255)
    number_of_pages = models.IntegerField('number of pages')
    pub_date = models.DateField(' date published')
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name='owner of the book')

    def __str__(self):
        return self.title

class CommonFields(models.Model):
    first_name = models.CharField('owner first name',max_length=50)
    last_name = models.CharField('owner last name',max_length=50) 
    address = models.CharField('owner address',max_length=100)
    phone = models.CharField('phone number', max_length=15)

    class Meta:
        abstract = True 

class Owner(CommonFields):
    # first_name = models.CharField('owner first name',max_length=50)
    # last_name = models.CharField('owner last name',max_length=50) 
    # address = models.CharField('owner address',max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_many_books(self):
        if len(self.book_set.all()) >= 5:
            return True 
        else:
            return False
    
    @property 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class UserProfile(CommonFields):
    bio = models.TextField(max_length=1000)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, verbose_name="user profile")
     
# Using proxy inheritance on book class
"""It inherits the table of the parent class but orders the entries"""
class OrderdBook(Book):
    class Meta:
        ordering=['title']
        proxy = True 

# Order books based on the authors 
class OrderBookByAuthor(Book):
    class Meta: 
        ordering=['author']

# Order the book owners based on firt name        
class OrderdOwner(Owner):
    class Meta:
        ordering = ['first_name']