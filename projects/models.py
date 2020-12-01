from django.db import models
from datetime import datetime
from author.models import Author
# Extending the core models
class Project(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=50)
    languages = models.CharField(max_length=70)
    
    tag1 = models.CharField(max_length=15, blank=True)
    tag2 = models.CharField(max_length=15, blank=True)
    tag3 = models.CharField(max_length=15, blank=True)
    shortDescription = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    github_link = models.CharField(max_length=200)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    project_date = models.DateTimeField(default=datetime.now, blank=True)

    # Display the main field in the admin area from the table
    def __str__(self):
        return f'{self.title} | {self.languages}'