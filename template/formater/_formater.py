from typing import Any

from rest_framework.generics import get_object_or_404

from constants import TemplateWidgets
from template.formater.widgets import ProgressBarWidget
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

    @staticmethod
    def _format_widgets(
            text: str, widgets: set[str], template_variables: dict[str, Any]
    ) -> str:
        for widget in widgets:
            match widget:
                case TemplateWidgets.progress_bar:
                    progress_bar_widget = ProgressBarWidget()
                    text = progress_bar_widget.format(text, template_variables)
        return text
