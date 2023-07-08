from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def search() -> dict:
    'Valute,Sell,Buy'
    try:
        browser = webdriver.Firefox()
        browser.get('https://www.tinkoff.ru/about/exchange/')
        time.sleep(2)
        assert 'Курсы валют' in browser.title
        el = browser.find_elements(By.CLASS_NAME, 'arod3t')
        result = dict(zip(['Valute','Sell','Buy'],el[1].text.split('\n')))
    except Exception as e:
        return e
    finally:
        browser.quit()
    return result


if __name__ == '__main__':
    print(search())