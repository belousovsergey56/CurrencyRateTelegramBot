import json
import requests

# API Central Bank
URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

"""
Module model, with basic methods for managing the api central bank. 
The main module uses these methods to translate the requested currency rate into a chat.
  
"""
def get_json(url) -> json:
    r = requests.get(url)
    return r.json(encoding='utf-8')


def list_currencies_to_print(json_: json) -> list:
    list_ = []
    for k, v in json_['Valute'].items():
        a = '{0} {1}'.format(k, v['Name'])
        list_.append(a)
    return list_


def currency_name_list(json_: json) -> list:
    list_ = []
    for k, v in json_['Valute'].items():
        a = '{0}'.format(k)
        list_.append(a)
    return list_


def get_currency_value(valute: str, json_=get_json(URL)) -> str:
    for k, v in json_['Valute'].items():
        if valute.casefold() == k.casefold():
            return "{0} {1}".format(k, v['Value'])
    return "Чтобы узнать курс, необходимо вести трёхбуквенное обозначение валюты."
