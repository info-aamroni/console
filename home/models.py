from django.db import models


# Create your models here
class Blogs(models.Model):
    title: models.TextField()
    slug: models.TextField()
    image: models.FileField()
    status: models.BooleanField()


