import json
import requests
from flask import Flask
from flask_sslify import SSLify
from flask import request
from app.valutes import list_currencies_to_print, get_currency_value, URL as U, get_json, currency_name_list

app = Flask('__name__')

# create https protocol
lify = SSLify(app)

URL = 'https://api.telegram.org/'
TOKEN = 'bot1337479154:AAHV1tBn8jHcSbUk6RbcRIA9M95FWjSYwGs/'


# send message bot to chat
def send_message(chat_id: str, text='Hola') -> json:
    url = URL + TOKEN + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

"""
Basic bot telegram method, receives messages from web hook, processes and sends the required message 
"""
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        help_meaasge = "Этот бот выводит актуальный курс валют по ЦБ относительно рубля.\n" \
                       "Посмотреть список доступной валюты, можно спомощью команды /list.\n" \
                       "Чтобы узнать курс доллара, нужно ввести стандартное обозначение этой единицы валюты: USD"
        list_valut = list_currencies_to_print(get_json(U))
        name_valut = currency_name_list(get_json(U))
        n = ''
        for k in name_valut:
            n += k + ','

        if '/start' in message:
            send_message(chat_id, 'Бот готов к работе. Если есть вопросы по его использованию, необходимо ввести /help')
        elif '/help' in message:
            send_message(chat_id, text=help_meaasge)
        elif '/list' in message:
            list = ''
            for k in list_valut:
                list += k + '\n'
            send_message(chat_id, text=list)
        elif message:
            send_message(chat_id, text=get_currency_value(message))
    return '<h1> Bot is started </h1>'


if __name__ == '__main__':
    app.run()
