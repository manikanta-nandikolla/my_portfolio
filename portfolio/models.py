from django.db import models

# Create your models here.

# Personal Details Model
class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="profile/")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)

    def __str__(self):
        return self.name

# Education Model
class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.degree} - {self.institution}"

# Skills Model
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Enter a value between 1-100")  # For progress bar

    def __str__(self):
        return self.name

# Projects Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# Contact Messages Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

