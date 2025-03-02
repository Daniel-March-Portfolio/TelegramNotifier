from typing import Any

from rest_framework.generics import get_object_or_404

from constants import TemplateWidgets
from template.formater.widgets import ProgressBarWidget, WidgetInterface
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
            self,
            text: str, widgets: set[str], template_variables: dict[str, Any]
    ) -> str:
        for widget_placeholder in widgets:
            widget = self._widgets_factory(widget_placeholder)
            text = widget.format(text, template_variables)
        return text

    def _widgets_factory(self, widget_placeholder: str) -> WidgetInterface:
        match widget_placeholder:
            case TemplateWidgets.progress_bar:
                return ProgressBarWidget()
            case _:
                raise NotImplementedError(
                    f'Widget {widget_placeholder} is not implemented'
                )