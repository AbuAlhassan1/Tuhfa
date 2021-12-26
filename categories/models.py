from datetime import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='categories-images/', null=True, blank=True)
    parent = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return "id = " + str(self.id) + " | name = " + self.name + " | parent id = " + str(self.parent)

class Theme(models.Model):
    name = models.CharField(max_length=32, null=True, default='Theme Name !', blank=True)
    title = models.CharField(max_length=32, null=True, default='Theme Title !', blank=True)
    description = models.TextField(max_length=500, null=True, blank=True, default="description ...")
    image = models.ImageField(upload_to='categories-images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, default=None, blank=True)
    date = models.DateField(editable=True, null=True, blank=True, default=datetime.now)

    def __str__(self):
        return self.name + str(self.id)