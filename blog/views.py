from django.shortcuts import render
from .models import Post, Comment
from django.db.models import Q
from .forms import SearchForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def results(request):
	filters = {}
	u = request.GET.get('user_id')
	c = request.GET.get('content')
	o = request.GET.get('order')

	if request.method == 'POST':
		form = SearchForm(request.POST or None)
		if form.is_valid():
			u = user
			c = content
		post_results = Post.objects.filter(**filters).order_by('datetime')
		return render(request, 'results.html', {'results':post_results})

	if request.method == 'GET':
		if u:
			filters['u'] = u
		if c:
			filters['c'] = c
		post_results = Post.objects.filter(**filters).order_by('datetime')
		return render(request, 'results.html', {'results':post_results})