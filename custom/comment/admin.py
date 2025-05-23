from django.contrib import admin
from .models import comment
# Register your models here.
@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'desc', 'created_on']