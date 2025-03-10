from uuid import UUID

import requests
from django.core.management.base import BaseCommand
from rest_framework.generics import get_object_or_404

from telegram.management.commands.utils import handle_response
from telegram.models import TelegramBot


class Command(BaseCommand):
    help = 'Send a message to a Telegram chat'

    def add_arguments(self, parser):
        parser.add_argument('--chat_id', type=int)
        parser.add_argument('--text', type=str)
        parser.add_argument('--bot_uuid', type=UUID)

    def handle(self, *args, **options) -> int:
        chat_id = options['chat_id']
        text = options['text']
        bot_uuid = options['bot_uuid']

        bot = self._get_bot(bot_uuid)
        message_id = self._send_message(chat_id, text, bot)
        return message_id

    def _get_bot(self, bot_uuid: UUID) -> TelegramBot:
        bot = get_object_or_404(TelegramBot, uuid=bot_uuid)
        return bot

    def _send_message(self, chat_id: int, text: str, bot: TelegramBot) -> int:
        url = f'https://api.telegram.org/bot{bot.token}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text,
        }
        response = requests.post(url, data=data)
        message_id = handle_response(response)
        return message_id
