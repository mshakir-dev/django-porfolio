from django.urls import path
# In order to define the path, we have to to bring the path
# URL FOR HOME PAGE

from . import views

urlpatterns = [
    # This is calling the index method from the views.py
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    # path('projects', views.projects, name='projects'),

]
