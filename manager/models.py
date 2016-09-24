from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ScriptlistModel(models.Model):
    author = models.CharField(max_length=30)
    tcid = models.CharField(max_length=30)
    scrfile = models.FileField(upload_to='documents/%Y/%m/%d')
    detail = models.TextField()
    now = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.scrfile.name


class CommentModel(models.Model):
    script = models.ForeignKey(ScriptlistModel) #ScriptlistModel
    writer = models.CharField(max_length=30)
    comments = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.script.tcid