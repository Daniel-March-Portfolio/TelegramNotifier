from dataclasses import dataclass
from typing import Any
from uuid import UUID

from django.db import models

from blank.models._blank import Blank


@dataclass(frozen=True)
class _Types:
    STRING = 'string'
    INTEGER = 'integer'
    FLOAT = 'float'
    BOOLEAN = 'boolean'
    UUID = 'uuid'


class BlankVariable(models.Model):
    types = _Types

    blank = models.ForeignKey(
        Blank, on_delete=models.CASCADE, related_name='variables'
    )
    key = models.CharField(max_length=64)
    _value = models.CharField(max_length=255, db_column='value')
    type = models.CharField(
        max_length=16, choices=(
            (_Types.STRING, 'String'),
            (_Types.INTEGER, 'Integer'),
            (_Types.FLOAT, 'Float'),
            (_Types.BOOLEAN, 'Boolean'),
            (_Types.UUID, 'UUID'),
        )
    )

    def __str__(self) -> str:
        return f'{self.key} - {self._value}'

    class Meta:
        unique_together = ['blank', 'key']
        indexes = [
            models.Index(fields=['blank']),
        ]

    @property
    def value(self) -> Any:
        match self.type:
            case _Types.INTEGER:
                return int(self._value)
            case _Types.FLOAT:
                return float(self._value)
            case _Types.BOOLEAN:
                return bool(self._value)
            case _Types.UUID:
                return UUID(self._value)
            case _:
                return self._value

    @value.setter
    def value(self, value: Any):
        self._value = str(value)