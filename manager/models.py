from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    author = models.CharField(max_length=30)
    tcid = models.CharField(max_length=30)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    detail = models.TextField()
    now = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.docfile