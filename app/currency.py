"""Module with basic methods for managing the api central bank."""
import json

from requests import get

URL_CENTRAL_BANK = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_json(url: str) -> json:
    """Use to get the json object.

    Function take URL and return json object

    Arguments:
        url: str

    Returns:
        json
    """
    return get(url).json()


def list_currencies_to_print(json_object: json) -> list:
    """Use to get list of currencies.

    Function take json object and append name currency to list
    Than return this list

    Arguments:
        json_object: json

    Returns:
        list
    """
    list_ = []
    for cut_name_currency, long_name in json_object['Valute'].items():
        template = '{0} {1}'.format(cut_name_currency, long_name['Name'])
        list_.append(template)
    return list_


def currency_name_list(json_object: json) -> list:
    """Use to return cut name currency.

    Helper function, returns the list of short names of the currency

    Arguments:
        json_object: json

    Returns:
        list
    """
    list_ = []
    for cut_currency_name, _ in json_object['Valute'].items():
        template = '{0}'.format(cut_currency_name)
        list_.append(template)
    return list_


def get_currency_value(currency_name: str) -> str:
    """Use to get the currency and its current exchange rate.

    The function takes a currency name and returns
    a string in the form of 'value name', for example 'USD 85.085'

    If the currency name is wrong, the function returns
    an explanation as string.

    Arguments:
        currency_name: str

    Returns:
        str
    """
    json_object = get_json(URL_CENTRAL_BANK)
    bad_answer = "Необходимо вести трёхбуквенное обозначение валюты."
    for cut_name_currency, currency_value in json_object['Valute'].items():
        if currency_name.casefold() == cut_name_currency.casefold():
            template = "{0} {1}"
            return template.format(cut_name_currency, currency_value['Value'])
    return bad_answer
