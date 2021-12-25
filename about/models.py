from django.db import models

class About(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    description = models.TextField(blank=True, null=True, default="Description ...")

    def __str__(self):
        return self.description
