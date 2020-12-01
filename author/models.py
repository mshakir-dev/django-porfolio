from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    my_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    resume = models.ImageField(upload_to='photos/File/%Y/%m/%d/', blank=True, null=True)
    summary = models.TextField(blank=True)
    phone = models.CharField(max_length=15)

    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    
    facebook = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    
    high_school = models.CharField(max_length=30, blank=True)
    high_school_title = models.CharField(max_length=150, blank=True)
    high_school_gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    high_school_graduated = models.CharField(max_length=50, blank=True)

    community_college = models.CharField(max_length=30, blank=True)
    community_college_title = models.CharField(max_length=150, blank=True)
    community_college_gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    community_college_graduated = models.CharField(max_length=50, blank=True)

    university = models.CharField(max_length=30, blank=True)
    university_title = models.CharField(max_length=150, blank=True)
    university_gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    university_graduated = models.CharField(max_length=50, blank=True)
    
    university_honors_list = models.CharField(max_length=150, blank=True)
    university_honors_list_link = models.CharField(max_length=150, blank=True)

    experience_1_company = models.CharField(max_length=50, blank=True)
    experience_1_position = models.CharField(max_length=50, blank=True)
    experience_1_description = models.TextField(blank=True)
    experience_1_hire_date = models.DateTimeField(default=datetime.now, blank=True)

    experience_2_company = models.CharField(max_length=50, blank=True)
    experience_2_position = models.CharField(max_length=50, blank=True)
    experience_2_description = models.TextField(blank=True)
    experience_2_hire_date = models.DateTimeField(default=datetime.now, blank=True)

    experience_3_company = models.CharField(max_length=50, blank=True)
    experience_3_position = models.CharField(max_length=50, blank=True)
    experience_3_description = models.TextField(blank=True)
    experience_3_hire_date = models.DateTimeField(default=datetime.now, blank=True)

    # Display the main field in the admin area from the table
    def __str__(self):
        return self.name