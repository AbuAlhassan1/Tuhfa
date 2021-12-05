from datetime import datetime
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=500)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, default=None, blank=True)

    def __str__(self):
        return str(self.id) + " | " + self.name + " | " + str(self.parent_id)

class Theme(models.Model):
    name = models.CharField(max_length=32, null=True, default='Theme Name !', blank=True)
    title = models.CharField(max_length=32, null=True, default='Theme Title !', blank=True)
    description = models.TextField(max_length=500, null=True, blank=True, default="description ...")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, default=None, blank=True)
    date = models.DateTimeField(editable=True, null=True, blank=True, default=datetime.now)



    def __str__(self):
        return self.name + str(self.id)