from django.contrib import admin
from .models import Post, Comment

# Registro de los modelos para que aparezcan en la administración de Django
admin.site.register(Post)
admin.site.register(Comment)
