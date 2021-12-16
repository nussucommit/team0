from rest_framework import serializers
from .models import Post
 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','title','content', 'datetime', 'likes']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','date_joined','last_login','is_admin']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','user','post','content', 'datetime', 'likes']