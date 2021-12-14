from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign-up', views.register, name="sign-up"),
    path('results', views.results, name="results")
]
