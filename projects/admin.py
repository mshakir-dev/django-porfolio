from django.contrib import admin
# Register your models here.
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'languages', 'is_published', 'project_date', 'shortDescription')
    list_display_links = ('id', 'title', 'is_published')
    search_fields = ('title', 'shortDescription')
    list_filter = ('author',)
    # The value of 'is_published' cannot be in both 'list_editable' and 'list_display_links'.
    # list_editable = ('is_published',)

admin.site.register(Project, ProjectAdmin)