from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign-up', views.register, name="sign-up"),
    path('results', views.results, name="results"),
    path('pread/<int:id>', views.pread, name="post_details"),
    path('pwrite', views.pwrite, name="create_post"),
    path('cwrite/<int:id>', views.cwrite.as_view(), name="create_comment"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
