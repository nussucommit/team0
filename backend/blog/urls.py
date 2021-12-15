from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign-up', views.register, name="sign-up"),
    path('results', views.results, name="results"),
    path('pread/<int:id>', views.pread, name="post_details"),
    path('pwrite', views.pwrite, name="create_post"),
    path('cwrite/<int:id>', views.cwrite.as_view(), name="create_comment"),
]
