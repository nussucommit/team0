from django import forms
from .models import Post, User, Comment


class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
	#user_id = forms.CharField(label='Username', min_length=1, max_length=64)
	#password = forms.CharField(label='Password', max_length=64, widget=PasswordInput)

class WritePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['user', 'title', 'content', 'likes']

class WriteCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['user', 'post', 'content', 'likes']
'''
class SignInForm(forms.Form):
	user_id = forms.CharField(label='Username', max_length=64)
	password = forms.CharField(label='Password', max_length=64, widget=PasswordInput)

class PostForm(forms.Form):
	title = forms.CharField(label='Post Title', max_length=64)
	content = forms.CharField(widget=Textarea)

class CommentForm(forms.Form):
	content = forms.CharField(widget=Textarea)
'''

#class SearchForm(forms.ModelForm):
#	class Meta:
#		model = Post
#		fields = ['user', 'content']