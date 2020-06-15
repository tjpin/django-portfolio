from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to="portfolio/imagelab/")
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(max_length=100, blank=True)
    objects = models.manager

    def __str__(self):
        return self.title
