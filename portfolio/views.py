from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    # tech_stack = project.tech_stack
    #split_tech_stack = tech_stack.split('/0')
    return render(request, 'portfolio/project_detail.html', {'project': project})