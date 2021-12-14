from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
	id = models.CharField(primary_key=True, max_length=64)
	password = models.CharField(max_length=64)

	def __str__(self):
		return self.id

'''
#Remove inheritence and opt for flatter RDB design
class Submission(models.Model):
	## Use automatic PK for submission_id
	content = models.TextField()
	datetime = models.DateTimeField(auto_now=True)
	likes = models.IntegerField()
'''

class Post(models.Model):
	#post = models.IntegerField(primary_key=True)
	#submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	content = models.TextField()
	datetime = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Comment(models.Model):
	#comment = models.IntegerField(primary_key=True)
	#submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField()
	datetime = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.content