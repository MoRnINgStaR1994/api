from django.urls import path
from . import views

urlpatterns = [
    path('get', views.get_plan, name='get_workout_plan'),
    path('create', views.create_plan, name='create_workout_plan'),
    path('achivment/add', views.set_current_achivment, name='add_achivment'),
    path('achivment/get', views.get_progress, name='get_achivment'),
]