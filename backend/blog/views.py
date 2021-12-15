from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView
from .forms import RegisterForm, WritePostForm, WriteCommentForm
from django.urls import reverse

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request, 'sign-up.html', {})

def results(request):
	filters = {}

	if request.method == 'POST':
		u = request.POST['username']
		c = request.POST['content']
		o = request.POST['order']
		if u:
			filters['user'] = u
		if c:
			filters['content'] = c
		post_results = Post.objects.filter(**filters)
		if o == '1':
			post_results = post_results.order_by('-datetime')

	if request.method == 'GET':
		post_results = Post.objects.order_by('-datetime')

	return render(request, 'results.html', {'results':post_results})

def pread(request, id):
	post = get_object_or_404(Post, pk=id)
	comments = Comment.objects.filter(post = id)
	return render(request, 'pread.html', {'post':post, 'comments':comments})

def pwrite(request):
	form = WritePostForm(request.POST or None)
	self_user = request.user
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('home')

	return render(request, 'pwrite.html', {'form':form, 'self':self_user})
'''
def cwrite(request, id):
	post = get_object_or_404(Post, pk=id)
	form = WriteCommentForm(request.POST or None)
	self_user = request.user
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('post_details')
	if request.method == 'GET':
		return render(request, 'cwrite.html', {'post':post})
'''
class cwrite(CreateView):
	model = Comment
	form_class = WriteCommentForm
	template_name = 'cwrite.html'

	def dispatch(self, request, *args, **kwargs):
		self.id = kwargs.get('id', 'default')
		return super(cwrite, self).dispatch(request, *args, **kwargs)

	def get_success_url(self):
		return reverse("post_details", kwargs={'id':str(self.object.post.id)})