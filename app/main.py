"""Start program."""
import json

from app.currency import (
    URL_CENTRAL_BANK,
    currency_name_list,
    get_currency_value,
    get_json,
    list_currencies_to_print,
)
from flask import Flask, request
from flask_sslify import SSLify
from requests import post

app = Flask('__name__')
ssl_certificate = SSLify(app)

TELEGRAM_URL = 'https://api.telegram.org/'
TELEGRAM_TKN = '2dea6508795e78bf1d75f4080a6ad5f685acc48afe0edb8199df3ad06cca3'
SEND_MESSAGE = 'sendMessage'
help_message = "Этот бот выводит актуальный курс валют по ЦБ относительно рубля.\n" \
               "Посмотреть список доступной валюты, можно спомощью команды /list.\n"\
               "Чтобы узнать курс доллара, нужно ввести стандартное обозначение этой единицы валюты: USD"
currency_list = list_currencies_to_print(get_json(URL_CENTRAL_BANK))
currency_name = currency_name_list(get_json(URL_CENTRAL_BANK))


def send_message(chat_id: str, text='Hola') -> json:
    """Use to send message to chat.

    The function accepts the chat identifier and the text entered by the user.
    It processes it and sends a message with the answer in json object format.

    Arguments:
        chat_id: str
        text: str

    Returns:
        json
    """
    url = TELEGRAM_URL + TELEGRAM_TKN + SEND_MESSAGE
    answer = {'chat_id': chat_id, 'text': text}
    response = post(url, json=answer)
    return response.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    """Use for dialog with user.

    The function uses a webhook, when a message from a user with a keyword is
    received, the script processes it and sends the user a reply.

    Returns:
        str
    """
    if request.method == 'POST':
        chat_id = request.get_json()['message']['chat']['id']
        message = request.get_json()['message']['text']

        empty_line = ''
        for name_key in currency_name:
            empty_line += name_key + ','
        if '/start' in message:
            send_message(chat_id, 'Бот готов к работе. Если есть вопросы по его использованию, необходимо ввести /help')
        elif '/help' in message:
            send_message(chat_id, text=help_message)
        elif '/list' in message:
            list_ = ''
            for name_key in currency_list:
                list_ += name_key + '\n'
            send_message(chat_id, text=list_)
        elif message:
            send_message(chat_id, text=get_currency_value(message))
    return '<h1> Bot is started </h1>'


if __name__ == '__main__':
    app.run()
