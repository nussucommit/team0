from django.shortcuts import render, redirect
from .models import Post, Comment
from django.db.models import Q
from .forms import RegisterForm, WritePostForm

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
			filters['username'] = u
		if c:
			filters['content'] = c
		post_results = Post.objects.filter(**filters)
		if o == '1':
			post_results = post_results.order_by('-datetime')

	if request.method == 'GET':
		post_results = Post.objects.order_by('-datetime')

	return render(request, 'results.html', {'results':post_results})

def pwrite(request):
	form = WritePostForm(request.POST or None)
	self_user = request.user
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('home')

	return render(request, 'pwrite.html', {'form':form, 'self': self_user})