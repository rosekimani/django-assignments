from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.author