from django.urls import path

from interests import views

app_name = 'interests'

urlpatterns = [
    path('', views.interests, name='interests'),
    path('<int:interest_id>/', views.interest_detail, name='interest_detail'),

]
