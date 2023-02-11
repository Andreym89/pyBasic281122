"""
Parser autoria
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://www.olx.ua/d/nedvizhimost/kvartiry/'

def get_html(url: str = URL):
    user_agent = {'User-agent': 'Mozilla/5.0 Chrome 109'}
    data = requests.get(url, headers=user_agent)

    if data.status_code == 200:
        print('Req status: ', data.status_code)
        return data.text
    return data.status_code

html_text = get_html()

# gоподключаем soup

soup = BeautifulSoup(html_text, 'html.parser')

all_items = soup.find_all("div", class_='css-1sw7q4x')

# print(all_cars.find('span', class_='link').text)
# print(all_items)
for item in all_items:
        print('Name: ', item.find('h6', class_='css-16v5mdi er34gjf0').text)
        print('Price: ', item.find('p', class_='css-10b0gli er34gjf0').text)
        print('Link: ', item.find('a', class_='css-rc5s2u'))

        #print(all_cars.find('div', class_='price-ticket').get('data-main-price'))



