from unittest import mock

import pytest
from rest_framework.test import APIClient

from telegram.models import TelegramBot
from template.models import Template


@pytest.mark.django_db
def test_api_send_notification(api_client: APIClient):
    test_template_body = 'Test {text}'
    test_template_tag = 'template_tag'
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
    with mock.patch(
            'telegram.management.commands.send_telegram_message.Command.handle'
    ) as mock_command:
        mock_command.return_value = 1
        api_client.post(
            '/notifications/notify/',
            {
                "template_tag": test_template_tag,
                "template_variables": {
                    "text": test_text
                },
                "chat_id": chat_id,
                "bot_uuid": bot.uuid
            },
            format='json',
        )
    expected_text = test_template_body.format(
        text=test_text,
    )
    mock_command.assert_called_once_with(
        chat_id=chat_id,
        text=expected_text,
        bot_uuid=bot.uuid,
    )
