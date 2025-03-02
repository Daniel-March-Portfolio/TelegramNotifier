import requests

from telegram.exceptions import (
    TelegramChatNotFoundException, TelegramBotNotFoundException,
    TelegramBotBlockedException, TelegramUserDeactivatedException,
    TelegramBadMessageException, TelegramMessageNotFoundException,
    TelegramMessageNotModifiedException
)


def handle_response(response: requests.Response) -> int:
    if response.status_code == 400:
        data = _try_parse_json(response)
        if data['description'] == 'Bad Request: chat not found':
            raise TelegramChatNotFoundException()
        if data['description'] == 'Bad Request: message text is empty':
            raise TelegramBadMessageException()
        if data['description'] == 'Bad Request: message text is empty':
            raise TelegramBadMessageException()
        if data['description'] == 'Bad Request: message text is empty':
            raise TelegramBadMessageException()
        if data['description'] == 'Bad Request: message to edit not found':
            raise TelegramMessageNotFoundException()
        if data['description'].startswith('Bad Request: message is not modified:'):
            raise TelegramMessageNotModifiedException()
    if response.status_code == 404:
        data = _try_parse_json(response)
        if data['description'] == 'Not Found':
            raise TelegramBotNotFoundException()
    if response.status_code == 403:
        data = _try_parse_json(response)
        if data['description'] == 'Forbidden: bot was blocked by the user':
            raise TelegramBotBlockedException()
        if data['description'] == 'Forbidden: user is deactivated':
            raise TelegramUserDeactivatedException()
    if response.status_code == 200:
        data = _try_parse_json(response)
        if data['ok']:
            return data['result']['message_id']
    response.raise_for_status()
    data = _try_parse_json(response)
    raise ValueError('Unknown error', data)


def _try_parse_json(response: requests.Response) -> dict:
    try:
        return response.json()
    except ValueError:
        raise ValueError('Response is not a JSON')
