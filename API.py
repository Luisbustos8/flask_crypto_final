from requests import Request, session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


base_url = "https://sandbox-api.coinmarketcap.com/v1/"
url_conversion = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol={}&convert=<{}>&CMC_PRO_API_KEY=<{}>".format("from_currency", "to_currency", "API")
parameters = {
    "start": "1",
    "limit": "",
    "convert": "EUR"
}
headers = {
    "Accepts" : "aplication/jason"
    "X-CMC_PRO_API_KEY" : "{}".format(API_KEY)
}

session = Session()
session.headers.update(headers)

try:
    response = sesion.get(url, params=parameters)
    data = json.loads(response.txt)
    print(data)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)