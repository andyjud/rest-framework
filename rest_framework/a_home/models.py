from django.db import models
from django.conf import settings

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
