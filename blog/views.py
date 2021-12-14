from django.shortcuts import render
from .models import Post, Comment
from django.db.models import Q
from .forms import RegisterForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def results(request):
	filters = {}

	if request.method == 'POST':
		u = request.POST['user_id']
		c = request.POST['content']
		o = request.POST['order']
		if u:
			filters['user_id'] = u
		if c:
			filters['content'] = c
		post_results = Post.objects.filter(**filters)
		if o == '1':
			post_results = post_results.order_by('-datetime')
		return render(request, 'results.html', {'results':post_results})

	if request.method == 'GET':
		post_results = Post.objects.filter(**filters).order_by('datetime')
		return render(request, 'results.html', {'results':post_results})