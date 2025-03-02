from typing import Any

from constants import TemplateWidgets
from template.formater.widgets.__interface import WidgetInterface


class ProgressBarWidget(WidgetInterface):
    def format(self, text: str, template_variables: dict[str, Any]) -> str:
        is_can_be_made = self._check_if_can_be_made(template_variables)
        if not is_can_be_made:
            return text
        progress = template_variables['progress']
        progress_bar = self._make(progress)
        return text.replace(TemplateWidgets.progress_bar, progress_bar)

    @staticmethod
    def _check_if_can_be_made(template_variables: dict[str, Any]) -> bool:
        if 'progress' not in template_variables:
            return False
        progress = template_variables['progress']
        if isinstance(progress, float):
            progress = round(progress)
        if not isinstance(progress, int):
            return False
        return True

    @staticmethod
    def _make(progress: int) -> str:
        size = 25
        progress = min(100, max(0, progress)) / 100
        n_fill_parts = round(size * progress)
        n_empty_parts = size - n_fill_parts
        fill_parts = '█' * n_fill_parts
        empty_parts = '░' * n_empty_parts
        return f'{fill_parts}{empty_parts}'
