from django.db import models

class Schedule(models.Model):
    Sunday = models.TextField(blank=True, null=True, default=None)
    Monday = models.TextField(blank=True, null=True, default=None)
    Tuesday = models.TextField(blank=True, null=True, default=None)
    Wednesday = models.TextField(blank=True, null=True, default=None)
    Thursday = models.TextField(blank=True, null=True, default=None)
    Friday = models.TextField(blank=True, null=True, default=None)
    Saturday = models.TextField(blank=True, null=True, default=None)

    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f" id = {self.id} || This Schedule Create At -> {self.created} || This Schedule Updated At -> {self.updated}"