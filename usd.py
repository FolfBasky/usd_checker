import requests
from bs4 import BeautifulSoup
from selenium_test import search

def usd_cbr():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'https://cbr.ru/currency_base/daily/'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    row = soup.find_all('tr')
    for el in row[1:]:
        if el.contents[1::2][1].text == 'USD':
            value = el.contents[1::2][4].text
            value = value.replace(',', '.')

    return round(float(value), 2)

def usd_tinkoff():
    data = search()
    return data['Sell']

def main():
    usd_value = usd_tinkoff()
    print(usd_value)


if __name__ == '__main__':
    main()  