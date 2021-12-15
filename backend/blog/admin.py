from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User, Post, Comment

class Admin(UserAdmin):
	list_display = ('username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('username',)
	read_only = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(User, Admin)
admin.site.register(Post)
admin.site.register(Comment)