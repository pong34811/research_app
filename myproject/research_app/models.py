from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class TagModel(models.Model):
    name = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_tags', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(User, related_name='updated_tags', on_delete=models.CASCADE, null=True, blank=True, editable=False)

    def __str__(self):
        return self.name

class ProjectModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    project_date = models.DateField()
    project_tag = models.ManyToManyField(TagModel, related_name='projects')
    image = models.ImageField(upload_to="img/")
    pdf_file = models.FileField(upload_to="pdf/")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_projects', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(User, related_name='updated_projects', on_delete=models.CASCADE, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = getattr(self, 'user', None)  # or another way to get current user
        self.updated_by = getattr(self, 'user', None)  # or another way to get current user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name
