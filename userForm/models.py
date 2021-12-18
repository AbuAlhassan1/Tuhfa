from django.db import models
from categories.models import Category, Theme

class UserForm(models.Model):
    full_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None)
    theme = models.ForeignKey(Theme, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return f"{self.full_name} || {str(self.id)}"
