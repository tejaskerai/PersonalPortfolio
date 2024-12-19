from django.urls import path, include
from . import views

app_name = 'education'

urlpatterns = [
    path('', views.education, name='education'),
]