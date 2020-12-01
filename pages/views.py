from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project
from author.models import Author
from experience.models import Experience
# It will import the dictionary from the Choice File
from projects.choices import projects_languages
# Create views here.

# def index(request):
#   return HttpResponse('<h2>Muhammad Shakir Portfolio</h2>')

def index(request):
  projects = Project.objects.order_by('-project_date').filter(is_published=True)[:3]
  context = {
    'projects': projects,
    'projects_languages': projects_languages
  }
  return render(request, 'pages/index.html', context)

def about(request):
  author = Author.objects.all()
  print(author)
  # It Will filter the Latest job at the First
  experiences = Experience.objects.order_by('-experience_hire_date')
  context = {
    'author': author,
    'experiences': experiences
  }
  return render(request, 'pages/about.html', context)