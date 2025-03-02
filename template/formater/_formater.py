from rest_framework.generics import get_object_or_404

from template.models import Template


class TemplateFormater:
    def __init__(self, template_tag: str):
        self._template_tag = template_tag

        self._check_if_template_exists()

    def _check_if_template_exists(self):
        get_object_or_404(Template, tag=self._template_tag)

    def format(self, **kwargs) -> str:
        template = Template.objects.get(tag=self._template_tag)
        text = template.body.format(**kwargs)
        return text
