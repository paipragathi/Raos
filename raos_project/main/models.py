from django.db import models

# main/models.py
from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.name

