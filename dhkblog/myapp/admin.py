from django.contrib import admin
from .models import BlogComment, Post,Contact

# Register your models here.
admin.site.register((Post,BlogComment,Contact))

