from django.db import models

from categories.models import Category

class Schedule(models.Model):
    day = models.TextField(max_length=10, null=True, blank=True, default="dayName")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="schedule_category", null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f" id = {self.id} || This Schedule Create At -> {self.created} || This Schedule Updated At -> {self.updated}"