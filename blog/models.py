from django.db import models

# Create your models here.
class User(models.Model):
	UserId = models.CharField(primary_key=True, max_length=64)
	Password = models.CharField(max_length=64)

	def __str__(self):
		return self.UserId

class Submission(models.Model):
	Content = models.TextField()
	DateTime = models.DateTimeField(auto_now=True)
	Likes = models.IntegerField()

class Post(Submission):
	## Use automatic PK for PostId
	UserId = models.ForeignKey(User, on_delete=models.CASCADE)
	Title = models.CharField(max_length=128)

	def __str__(self):
		return self.Title

class Comment(Submission):
	## Use automatic PK for CommentId
	PostId = models.ForeignKey(Post, on_delete=models.CASCADE)
	UserId = models.ForeignKey(User, on_delete=models.CASCADE)