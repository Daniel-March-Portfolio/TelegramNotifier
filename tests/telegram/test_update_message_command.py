import pytest

from telegram.exceptions import (
    TelegramBadMessageException, TelegramMessageNotFoundException,
    TelegramMessageNotModifiedException
)
from telegram.management.commands.update_telegram_message import Command
from telegram.models import TelegramBot

_MESSAGE_TEXT = 'test message'


@pytest.mark.django_db
def test_update_message_command(test_token: str, test_chat_id: int):
    bot = TelegramBot(
        name='test_bot',
        token=test_token,
    )
    bot.save()
    message_id = send_message(
        bot=bot,
        test_chat_id=test_chat_id,
    )
    command = Command()
    command.handle(
        message_id=message_id,
        chat_id=test_chat_id,
        text=_MESSAGE_TEXT + ' updated',
        bot_uuid=bot.uuid,
    )


@pytest.mark.django_db
def test_update_message_command__message_not_found(
        test_token: str, test_chat_id: int
):
    bot = TelegramBot(
        name='test_bot',
        token=test_token,
    )
    bot.save()

    command = Command()
    with pytest.raises(TelegramMessageNotFoundException):
        command.handle(
            message_id=10 ** 1000,  # Totally unrealistic chat_id
            chat_id=test_chat_id,
            text='test message',
            bot_uuid=bot.uuid,
        )


@pytest.mark.django_db
def test_update_message_command__bad_message(
        test_token: str, test_chat_id: int
):
    bot = TelegramBot(
        name='test_bot',
        token=test_token,
    )
    bot.save()
    message_id = send_message(
        bot=bot,
        test_chat_id=test_chat_id,
    )

    command = Command()
    with pytest.raises(TelegramBadMessageException):
        command.handle(
            message_id=message_id,
            chat_id=test_chat_id,
            text='',
            bot_uuid=bot.uuid,
        )


@pytest.mark.django_db
def test_update_message_command__not_modified(
        test_token: str, test_chat_id: int
):
    bot = TelegramBot(
        name='test_bot',
        token=test_token,
    )
    bot.save()
    message_id = send_message(
        bot=bot,
        test_chat_id=test_chat_id,
    )

    command = Command()
    with pytest.raises(TelegramMessageNotModifiedException):
        command.handle(
            message_id=message_id,
            chat_id=test_chat_id,
            text=_MESSAGE_TEXT,
            bot_uuid=bot.uuid,
        )


def send_message(bot: TelegramBot, test_chat_id: int) -> int:
    from telegram.management.commands.send_telegram_message import Command
    command = Command()
    message_id = command.handle(
        chat_id=test_chat_id,
        text=_MESSAGE_TEXT,
        bot_uuid=bot.uuid,
    )
    return message_id
