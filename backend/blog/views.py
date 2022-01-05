from .serializers import PostSerializer, UserSerializer, CommentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from .models import Post, User, Comment

class results(generics.ListAPIView):
	serializer_class = PostSerializer
	permission_classes = [IsAuthenticated]
	def get_queryset(self, *args, **kwargs):
		queryset = Post.objects.all()
		if self.request.query_params.get('username'):
			#note: icontains does not work for FK or other fields that have choices
			#if required, can create temporary deep copy to query against
			queryset = queryset.filter(user=self.request.query_params.get('username'))
		if self.request.query_params.get('content'):
			queryset = queryset.filter(content__icontains=self.request.query_params.get('content'))
		if self.request.query_params.get('order') == '1':
			queryset = queryset.order_by('-datetime')
		return queryset

class cr_post(generics.CreateAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = PostSerializer
	queryset = Post.objects.all()

class cr_comments(generics.CreateAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

class post(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class postcomments(generics.ListAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = CommentSerializer

	#use custom queryset instead of custom lookup_field to maintain same serializer with commentView
	def get_queryset(self, *args, **kwargs):
		return Comment.objects.filter(post=self.kwargs['post'])

class comment(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()


#Depreciated code:
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

class MultipleFieldLookupMixin:
    #Apply this mixin to any view or viewset to get multiple field filtering
    #based on a `lookup_fields` attribute, instead of the default single field filtering.

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
'''
