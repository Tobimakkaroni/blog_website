from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(Post, PostAdmin)
