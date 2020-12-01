from django.db import models
from datetime import datetime
from author.models import Author

class Service(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    service_icon = models.CharField(max_length=100, blank=True)
    service_languages = models.CharField(max_length=100, blank=True)
    service_description = models.TextField(blank=True)

    # Display the main field in the admin area from the table
    def __str__(self):
        return self.service_languages