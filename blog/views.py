from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def results(request):
	if request.method == 'GET':
		post_results = Post.objects.all
		return render(request, 'results.html', {'results':post_results})