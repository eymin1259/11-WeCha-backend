from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('/email', views.EmaliDuplicationCheck.as_view()),
    path('/signup', views.SignUp.as_view()),
    path('/signin', views.SignIn.as_view()),
]