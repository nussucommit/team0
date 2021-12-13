from django.db import models

# Create your models here.
class User(models.Model):
	user = models.CharField(primary_key=True, max_length=64)
	password = models.CharField(max_length=64)

	def __str__(self):
		return self.user

class Submission(models.Model):
	content = models.TextField()
	datetime = models.DateTimeField(auto_now=True)
	likes = models.IntegerField()

class Post(Submission):
	## Use automatic PK for PostId
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)

	def __str__(self):
		return self.title

class Comment(Submission):
	## Use automatic PK for CommentId
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)