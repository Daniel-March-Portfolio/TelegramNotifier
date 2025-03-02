from typing import Any

from rest_framework.generics import get_object_or_404

from constants import TemplateWidgets
from template.models import Template


class TemplateFormater:
    def __init__(self, template_tag: str):
        self._template_tag = template_tag

        self._check_if_template_exists()

    def _check_if_template_exists(self):
        get_object_or_404(Template, tag=self._template_tag)

    def format(self, template_variables: dict[str, Any]) -> str:
        template = Template.objects.get(tag=self._template_tag)
        text = template.body
        text = self._format_widgets(
            text, template.used_widgets, template_variables
        )
        text = text.format(**template_variables)
        return text

    def _format_widgets(
            self, text: str, widgets: set[str], template_variables
    ) -> str:
        for widget in widgets:
            match widget:
                case TemplateWidgets.progress_bar:
                    text = self._format_progres_bar_widget(
                        text, template_variables
                    )
        return text

    def _format_progres_bar_widget(self, text: str, template_variables) -> str:
        progress_widget_is_valid = self._check_if_progress_widget_is_valid(
            **template_variables
        )
        if not progress_widget_is_valid:
            return text
        progress = template_variables['progress']
        progress_bar = self._create_progress_bar(progress)
        return text.replace(TemplateWidgets.progress_bar, progress_bar)

    def _check_if_progress_widget_is_valid(self, **kwargs) -> bool:
        if 'progress' not in kwargs:
            return False
        progress = kwargs['progress']
        if isinstance(progress, float):
            progress = round(progress)
        if not isinstance(progress, int):
            return False
        return True

    @staticmethod
    def _create_progress_bar(progress: int) -> str:
        size = 25
        progress = min(100, max(0, progress)) / 100
        n_fill_parts = round(size * progress)
        n_empty_parts = size - n_fill_parts
        fill_parts = '█' * n_fill_parts
        empty_parts = '░' * n_empty_parts
        return f'{fill_parts}{empty_parts}'
