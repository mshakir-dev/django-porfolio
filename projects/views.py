from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, Page
from .choices import projects_languages

from . models import Project


# Create your views here.

def index(request):
    # Fetch the data
    # projects = Project.objects.all()
    projects = Project.objects.order_by('-project_date').filter(is_published=True)

    paginator = Paginator(projects, 6)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    
    context = {
        # 'projects': projects
        'projects': paged_projects
    }
    
    return render(request, 'projects/projects.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'projects/project.html', context)


def search(request):
    queryset_list = Project.objects.order_by('-project_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # description is coming from the database
            queryset_list =  queryset_list.filter(description__icontains=keywords) 

    if 'languages' in request.GET:
        languages = request.GET['languages']
        if languages:
            # tag1 is coming from the database and languages is the name in the html
            queryset_list = queryset_list.filter(tag1__iexact=languages)

    context = {
        'projects_languages': projects_languages,
        'projects': queryset_list,
        'values': request.GET
    }
    return render(request, 'projects/search.html', context)
