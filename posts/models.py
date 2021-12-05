from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title       = models.CharField(max_length=255)
    description = RichTextField(blank=True, config_name='awesome_ckeditor', default='')
    image       = models.ImageField(upload_to='images/', null=True, blank=True)
    created_on  = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Created on')
    updated_on  = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated on')

    def __str__(self):
        return  str(self.created_on).split('.')[0] + ' || ' + self.title