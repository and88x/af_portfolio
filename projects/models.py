from django.db import models

# Create your models here.
class Project(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    technology  = models.CharField(max_length=20)
    image       = models.FilePathField(path="/img")

# Create your models here.
class Portfolio(models.Model):
    title        = models.CharField(max_length=100)
    sdescription = models.TextField()
    ldescription = models.TextField()
    technology   = models.CharField(max_length=30)
    image        = models.FilePathField(path="/img")
    link         = models.URLField(max_length=200)

# Create your models here.
class My_Portfolio(models.Model):
    title        = models.CharField(max_length=100)
    sdescription = models.TextField()
    ldescription = models.TextField()
    technology   = models.CharField(max_length=30)
    image        = models.FilePathField(path="/img")
    second_img   = models.FilePathField(path="/img")
    link         = models.URLField(max_length=200)