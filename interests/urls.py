from django.urls import path

from interests import views

app_name = 'interests'

urlpatterns = [
    path('', views.interests, name='interests'),
    path('photoshop/', views.photoshop, name='photoshop'),

]
