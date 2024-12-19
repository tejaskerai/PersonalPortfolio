from django.urls import path, include
from . import views

app_name = 'experience'

urlpatterns = [
    path('', views.experience, name='experience'),
]