from uuid import UUID

import requests
from django.core.management.base import BaseCommand

from telegram.exceptions import TelegramChatNotFoundException, \
    TelegramBotNotFoundException, TelegramBotBlockedException, \
    TelegramUserDeactivatedException, TelegramBadMessageException
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

        bot = TelegramBot.objects.get(uuid=bot_uuid)
        message_id = self._send_message(chat_id, text, bot)
        return message_id

    def _send_message(self, chat_id: int, text: str, bot: TelegramBot) -> int:
        url = f'https://api.telegram.org/bot{bot.token}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text,
        }
        response = requests.post(url, data=data)
        message_id = self._handle_response(response)
        return message_id

    def _handle_response(self, response: requests.Response) -> int:
        if response.status_code == 400:
            data = self._try_parse_json(response)
            if data['description'] == 'Bad Request: chat not found':
                raise TelegramChatNotFoundException()
            if data['description'] == 'Bad Request: message text is empty':
                raise TelegramBadMessageException()
        if response.status_code == 404:
            data = self._try_parse_json(response)
            if data['description'] == 'Not Found':
                raise TelegramBotNotFoundException()
        if response.status_code == 403:
            data = self._try_parse_json(response)
            if data['description'] == 'Forbidden: bot was blocked by the user':
                raise TelegramBotBlockedException()
            if data['description'] == 'Forbidden: user is deactivated':
                raise TelegramUserDeactivatedException()
        if response.status_code == 200:
            data = self._try_parse_json(response)
            if data['ok']:
                return data['result']['message_id']
        response.raise_for_status()
        data = self._try_parse_json(response)
        raise ValueError('Unknown error', data)

    def _try_parse_json(self, response: requests.Response) -> dict:
        try:
            return response.json()
        except ValueError:
            raise ValueError('Response is not a JSON')