from abc import ABC, abstractmethod
from typing import Any


class WidgetInterface(ABC):
    @abstractmethod
    def format(self, text: str, template_variables: dict[str, Any]) -> str: ...
