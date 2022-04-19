# CurrencyTracker

import requests
import webbrowser
from bs4 import BeautifulSoup

service_url = 'https://doviz.com'
html_text = requests.get(service_url).text
soup = BeautifulSoup(html_text, 'html.parser')

usdData = soup.find('span', attrs = {
    'data-socket-key': 'USD'
})
usd_currency = usdData.decode_contents()
usd_description_result = "1 Dolar = " + usd_currency

euroData = soup.find('span', attrs = {
    'data-socket-key': 'EUR'
})
eur_currency = euroData.decode_contents()
eur_description_result = "1 Euro = " + eur_currency

btcData = soup.find('span', attrs = {
    'data-socket-key': 'bitcoin'
})

btc_currency = btcData.decode_contents()
btc_description_result = "1 Bitcon = " + btc_currency

print(eur_description_result)
print(usd_description_result)
print(btc_description_result)
