import requests
import json
from config import exchanges

class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {quote}')

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена!')

        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise APIException(f'Валюта {quote} не найдена!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_quote = json.loads(r.content)[exchanges[quote]] * float(amount)

        return total_quote

