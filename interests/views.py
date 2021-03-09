from django.shortcuts import render, get_object_or_404


# Create your views here.

# Create your views here.
from interests.models import Interest


def interests(request):
    interests = Interest.objects.all()
    return render(request, 'interests/interests.html', {'interests':interests})

def interest_detail(request, interest_id):
    interest = get_object_or_404(Interest, pk=interest_id)
    return render(request, 'interests/interest_detail.html', {'interest':interest})
