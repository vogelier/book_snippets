from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You are at the snippets app.")


# Class based views

# See all snippets

# See one snippet

# See all books snippets are from

# See all authors snippets are from

# Search snippets

# Subscribe to snippets email