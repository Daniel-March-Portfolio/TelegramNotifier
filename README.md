# TelegramNotifier

This is a simple Telegram application, that allows you to send
prepared messages to your Telegram chats.

For example, you can send a message to your chat, when your
application is deployed, or notify about progress of some
long-running task.

## Features
* Send prepared messages to your chats
* Send messages with progress indicator
* Use different bots for different notifications

## Usage example

1. Create bot.
2. Add bot to target chat.
3. Add bot in admin panel.
4. Create a template.
5. Create a blank
   * Select created template. 
   * Select created bot. 
   * Set target chat id. 
   * Fill variables if needed.
6. Send a message like this:

```shell
curl 'http://127.0.0.1:8000/blanks/send/' --header 'Content-Type: application/json' --data '{"blank_tag": "some_server_deploy_started"}'
```

## Preview

![Bot editor](https://github.com/Daniel-March-Portfolio/.github/blob/main/images/TelegramNotifier/bot_edit.png)

![Template editor](https://github.com/Daniel-March-Portfolio/.github/blob/main/images/TelegramNotifier/template_edit.png)

![Blank editor](https://github.com/Daniel-March-Portfolio/.github/blob/main/images/TelegramNotifier/blank_edit.png)

![Message example](https://github.com/Daniel-March-Portfolio/.github/blob/main/images/TelegramNotifier/message_example.png)
