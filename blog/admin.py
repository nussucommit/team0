from django.contrib import admin

# Register your models here.
from .models import User, Submission, Post, Comment

admin.site.register(User)
admin.site.register(Submission)
admin.site.register(Post)
admin.site.register(Comment)