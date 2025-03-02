from uuid import uuid4

from django.db import models

from constants import TemplateWidgets


class Template(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)

    tag = models.CharField(max_length=64, unique=True)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=['tag']),
        ]

    @property
    def used_widgets(self) -> set[str]:
        used_widgets = set()
        for widget_placeholder in TemplateWidgets.ALL:
            if widget_placeholder in self.body:
                used_widgets.add(widget_placeholder)
        return used_widgets
