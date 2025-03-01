from uuid import uuid4

from django.db import models

class Template(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)

    tag = models.CharField(max_length=64)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=['tag']),
        ]