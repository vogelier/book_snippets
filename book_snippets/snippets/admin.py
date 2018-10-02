from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Source)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Snippet)
