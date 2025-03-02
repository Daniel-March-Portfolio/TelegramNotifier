import pytest

from template.formater import TemplateFormater
from template.models import Template


@pytest.mark.django_db
def test_template_used_widgets():
    template = Template(
        tag="test_template",
        body="Test\n|{{PROGRESS_BAR}}|",
    )
    template.save()

    formater = TemplateFormater(template_tag=template.tag)
    text = formater.format({'progress': 40})

    expected_text = (
        "Test\n"
        "|██████████░░░░░░░░░░░░░░░|"
    )
    assert text == expected_text
