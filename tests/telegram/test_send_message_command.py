from unittest import mock

import pytest

from telegram.exceptions import (
    TelegramChatNotFoundException, TelegramBotNotFoundException,
    TelegramBotBlockedException, TelegramUserDeactivatedException,
    TelegramBadMessageException
)
from telegram.management.commands.send_telegram_message import Command
from telegram.models import TelegramBot


@pytest.mark.django_db
def test_send_message_command(test_token: str, test_chat_id: int):
    bot = TelegramBot(
        name='test_bot',
        token=test_token,
    )
    bot.save()

    command = Command()
    command.handle(
        chat_id=test_chat_id,
        text='test message',
        bot_uuid=bot.uuid,
    )


@pytest.mark.django_db
def test_send_message_command__chat_not_found(test_token: str):
    bot = TelegramBot(
        name='test_bot',
        token=test_token,
    )
    bot.save()

    command = Command()
    with pytest.raises(TelegramChatNotFoundException):
        command.handle(
            chat_id=10 ** 1000,  # Totally unrealistic chat_id
            text='test message',
            bot_uuid=bot.uuid,
        )


@pytest.mark.django_db
def test_send_message_command__bot_not_found():
    bot = TelegramBot(
        name='test_bot',
        token='test_token',
    )
    bot.save()

    command = Command()
    with pytest.raises(TelegramBotNotFoundException):
        command.handle(
            chat_id=123,
            text='test message',
            bot_uuid=bot.uuid,
        )


@pytest.mark.django_db
def test_send_message_command__bot_blocked():
    bot = TelegramBot(
        name='test_bot',
        token='test_token',
    )
    bot.save()

    command = Command()
    with (
        pytest.raises(TelegramBotBlockedException),
        mock.patch('requests.post') as mock_request,
    ):
        mock_request.return_value.status_code = 403
        mock_request.return_value.json.return_value = {
            'description': 'Forbidden: bot was blocked by the user',
        }
        command.handle(
            chat_id=123,
            text='test message',
            bot_uuid=bot.uuid,
        )


@pytest.mark.django_db
def test_send_message_command__user_deactivated():
    bot = TelegramBot(
        name='test_bot',
        token='test_token',
    )
    bot.save()

    command = Command()
    with (
        pytest.raises(TelegramUserDeactivatedException),
        mock.patch('requests.post') as mock_request,
    ):
        mock_request.return_value.status_code = 403
        mock_request.return_value.json.return_value = {
            'description': 'Forbidden: user is deactivated',
        }
        command.handle(
            chat_id=123,
            text='test message',
            bot_uuid=bot.uuid,
        )


@pytest.mark.django_db
def test_send_message_command__bad_message(test_token: str, test_chat_id: int):
    bot = TelegramBot(
        name='test_bot',
        token=test_token,
    )
    bot.save()

    command = Command()
    with pytest.raises(TelegramBadMessageException):
        command.handle(
            chat_id=test_chat_id,
            text='',
            bot_uuid=bot.uuid,
        )
