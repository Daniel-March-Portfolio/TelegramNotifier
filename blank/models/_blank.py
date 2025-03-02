from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models

from telegram.models import TelegramBot
from template.models import Template


class Blank(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    tag = models.CharField(max_length=64, unique=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    bot = models.ForeignKey(TelegramBot, on_delete=models.CASCADE)
    _chat_id = models.CharField(
        max_length=64,
        validators=[RegexValidator(r'^\d+$')],
        db_column='chat_id'
    )

    def __str__(self) -> str:
        return f'{self.template.tag} - {self._chat_id}'

    class Meta:
        indexes = [
            models.Index(fields=['tag']),
        ]

    @property
    def chat_id(self) -> int:
        return int(self._chat_id)

    @chat_id.setter
    def chat_id(self, value: int):
        if not isinstance(value, int):
            raise ValueError('chat_id must be an integer')
        self._chat_id = str(value)

    @property
    def template_variables(self) -> dict[str, str]:
        return {
            variable.key: variable.value
            for variable in self.variables.all()
        }

    def save(self, *args, **kwargs):
        if not self._chat_id:
            raise ValueError('chat_id cannot be empty')
        super().save(*args, **kwargs)
