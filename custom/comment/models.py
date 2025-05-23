from django.db import models

# Create your models here.
class comment(models.Model):
    desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)