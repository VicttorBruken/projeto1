from django.contrib import admin

# Import the model
from .models import Post

# Register your models here.
admin.site.register(Post)