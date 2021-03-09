from django.shortcuts import render, get_object_or_404


# Create your views here.

# Create your views here.
from interests.models import Interest


def interests(request):
    interests = Interest.objects.all()
    return render(request, 'interests/interests.html', {'interests':interests})

def photoshop(request):
    return render(request, 'interests/photoshop.html')
