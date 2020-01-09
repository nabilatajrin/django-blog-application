from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.TextField()
    slugs = models.SlugField(null=True)
    content = models.TextField(null=True, blank=True)





