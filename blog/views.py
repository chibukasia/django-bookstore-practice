from django.shortcuts import render 
from .models.author import Author 
from .models.blog import Blog 
from .models.entry import Entry 

# Create your views here.
def index(request):
    pass 


def create_author(request):
    # author = Author.objects.create()
    pass

def blog_entries(request):
    # entries = Entry.objects.filter(blog__name="The beatles song")
    pass 