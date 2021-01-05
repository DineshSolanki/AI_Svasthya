import json
from telegram import Bot


def notify_bot(message):
    with open('../ignored/keys.json', 'r') as keys_file:
        k = json.load(keys_file)
        token = k['telegram_token']
        chat_id = k['telegram_chat_id']
        bot = Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)
