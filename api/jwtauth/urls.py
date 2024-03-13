from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='token_obtain_pair'),
    path('signup', views.signup, name='token_refresh'),
]