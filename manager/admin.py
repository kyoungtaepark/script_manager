from django.contrib import admin
from .models import ScriptlistModel, CommentModel
# Register your models here.

admin.site.register(ScriptlistModel)
admin.site.register(CommentModel)