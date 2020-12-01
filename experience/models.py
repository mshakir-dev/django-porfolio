from django.db import models
from datetime import datetime
from author.models import Author

class Experience(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    experience_company = models.CharField(max_length=50, blank=True)
    experience_position = models.CharField(max_length=50, blank=True)
    experience_desc_point1 = models.CharField(max_length=100, blank=True)
    experience_desc_point2 = models.CharField(max_length=100, blank=True)
    experience_desc_point3 = models.CharField(max_length=100, blank=True)
    experience_desc_point4 = models.CharField(max_length=100, blank=True)
    experience_desc_point5 = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50, blank=True)
    experience_hire_date = models.DateTimeField(blank=True)
    experience_end_date = models.DateTimeField(blank=True)
    # Display the main field in the admin area from the table
    def __str__(self):
        return self.experience_company