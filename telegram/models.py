from uuid import uuid4

from django.db import models


class TelegramBot(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.name
