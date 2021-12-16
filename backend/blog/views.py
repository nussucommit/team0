from .serializers import PostSerializer, UserSerializer, CommentSerializer
from rest_framework import generics
from .models import Post, User, Comment

class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class results(MultipleFieldLookupMixin, generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	lookup_fields = ['username', 'content']

class post(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class comment(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


'''
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import PostSerializer
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView
from .forms import RegisterForm, WritePostForm, WriteCommentForm
from django.urls import reverse
'''

'''
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

class cwrite(CreateView):
	model = Comment
	form_class = WriteCommentForm
	template_name = 'cwrite.html'

	def dispatch(self, request, *args, **kwargs):
		self.id = kwargs.get('id', 'default')
		return super(cwrite, self).dispatch(request, *args, **kwargs)

	def get_success_url(self):
		return reverse("post_details", kwargs={'id':str(self.object.post.id)})
'''