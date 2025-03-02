from unittest import mock

import pytest
from rest_framework.test import APIClient

from blank.models import Blank, BlankVariable
from telegram.models import TelegramBot
from template.models import Template


@pytest.mark.django_db
def test_api_send_blank_notification(api_client: APIClient):
    test_template_body = 'Test {text} {blank_text}'
    test_template_tag = 'template_tag'
    test_blank_tag = 'blank_tag'
    blank_text = 'blank_text'
    test_text = '123'
    chat_id = 123

    template = Template(
        tag=test_template_tag,
        body=test_template_body,
    )
    template.save()

    bot = TelegramBot(
        name='name',
        token='token',
    )
    bot.save()

    blank = Blank(
        tag=test_blank_tag,
        template=template,
        bot=bot,
        chat_id=chat_id,
    )
    blank.save()
    BlankVariable(
        blank=blank,
        key='blank_text',
        value=blank_text,
        type=BlankVariable.types.STRING,
    ).save()

    with mock.patch(
            'telegram.management.commands.send_telegram_message.Command.handle'
    ) as mock_command:
        mock_command.return_value = 1
        response = api_client.post(
            '/blanks/send/',
            {
                "blank_tag": test_blank_tag,
                "template_variables": {
                    "text": test_text
                },
            },
            format='json',
        )
        assert response.status_code == 200, response.text
    expected_text = test_template_body.format(
        text=test_text,
        blank_text=blank_text
    )
    mock_command.assert_called_once_with(
        chat_id=chat_id,
        text=expected_text,
        bot_uuid=bot.uuid,
    )
