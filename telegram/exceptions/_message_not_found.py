class TelegramMessageNotFoundException(Exception):
    def __init__(self):
        super().__init__('Message not found')
