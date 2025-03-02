import pytest

from constants import TemplateWidgets
from template.models import Template


@pytest.mark.django_db
def test_template_used_widgets():
    template = Template(
        tag="test_template",
        body="Hello {name}, your progress is {progress} {{PROGRESS_BAR}}",
    )
    template.save()

    assert template.used_widgets == {TemplateWidgets.progress_bar}