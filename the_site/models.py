from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    short_description = models.TextField()
    image = models.CharField(max_length=200)
    url = models.URLField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_name

class navItem(models.Model):
    item_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name