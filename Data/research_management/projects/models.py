# models.py
from django.db import models

class ResearchProject(models.Model):
    project_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.project_name


# models.py


class Tag(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    event_name = models.CharField(max_length=100, default="")
    event_tag = models.ManyToManyField(Tag, limit_choices_to={'is_active': True})

    def __str__(self):
        return self.event_name

