import os

from pytest import fixture


@fixture
def test_token() -> str:
    test_telegram_bot_token = os.getenv('TEST_TELEGRAM_BOT_TOKEN')
    if test_telegram_bot_token is None:
        raise ValueError('TEST_TELEGRAM_BOT_TOKEN is not set')
    return test_telegram_bot_token


@fixture
def test_chat_id() -> int:
    test_telegram_bot_chat_id = os.getenv('TEST_TELEGRAM_BOT_CHAT_ID')
    if test_telegram_bot_chat_id is None:
        raise ValueError('TEST_TELEGRAM_BOT_CHAT_ID is not set')
    if not test_telegram_bot_chat_id.isdigit():
        raise ValueError('TEST_TELEGRAM_BOT_CHAT_ID is not a number')
    test_telegram_bot_chat_id = int(test_telegram_bot_chat_id)
    return test_telegram_bot_chat_id
