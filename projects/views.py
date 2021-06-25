from django.shortcuts import render
from projects.models import My_Portfolio

# Create your views here.
def project_index(request):
    projects = My_Portfolio.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = My_Portfolio.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)