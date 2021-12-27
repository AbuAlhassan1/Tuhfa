from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    description = RichTextField(blank=True, null=True, default="Description ...")
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} || {self.description}"
