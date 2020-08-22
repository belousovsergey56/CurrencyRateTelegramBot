import requests

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_json(url):
    r = requests.get(url)
    return r.json(encoding='utf-8')


def list_valutes_for_print_users(json_):
    list_ = []
    for k, v in json_['Valute'].items():
        a = '{0} {1}'.format(k, v['Name'])
        list_.append(a)
    return list_


def valutes_name_list(json_):
    list_ = []
    for k, v in json_['Valute'].items():
        a = '{0}'.format(k)
        list_.append(a)
    return list_


def get_valute_value(valute, json_=get_json(URL)):
    for k, v in json_['Valute'].items():
        if valute.casefold() == k.casefold():
            return "{0} {1}".format(k, v['Value'])
    return "Чтобы узнать курс, необходимо вести трёхбуквенное обозначение валюты."
