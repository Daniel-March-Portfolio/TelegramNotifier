class TelegramChatNotFoundException(Exception):
    def __init__(self):
        super().__init__('Chat not found')
