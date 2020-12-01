from django.urls import path
# In order to define the path, we have to to bring the path
# URL FOR HOME PAGE

from . import views

urlpatterns = [
    # This is calling the index method from the views.py
    # If there is no path then it will pretend /projects
    path('', views.index, name='projects'),
    # This path will add the parameter such projects/68
    path('<int:project_id>', views.project, name='project'),
    path('search', views.search, name='search'),
]
