from django.urls import path, include
from . import views
#from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('results', views.results.as_view(), name='show_posts'),
    path('post/create', views.cr_post.as_view(), name='create_post'),
    path('post/<int:pk>', views.post.as_view(), name='post'),
    path('post/comments/<int:post>', views.postcomments.as_view(), name='show_comments'),
    path('comment/create', views.cr_comments.as_view(), name='create_post'),
    path('comment/<int:pk>', views.comment.as_view(), name='comment'),
    
    #Authorization
    path('auth/' , include('djoser.urls')), 
    path('auth/' , include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

'''
    path('', views.home, name="home"),
    path('sign-up', views.register, name="sign-up"),
    path('results', views.results, name="results"),
    path('pread/<int:id>', views.pread, name="post_details"),
    path('pwrite', views.pwrite, name="create_post"),
    path('cwrite/<int:id>', views.cwrite.as_view(), name="create_comment"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
'''
