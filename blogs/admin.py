from django.contrib import admin

# Register your models here.
from .models import Blog, Article

admin.site.register(Blog)
admin.site.register(Article)