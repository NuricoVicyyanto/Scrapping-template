from bs4 import BeautifulSoup
import requests
import csv

website = 'https://www.tiket.com/hotel/search?room=1&adult=1&page=1&id=surabaya-108001534490276270&type=CITY&q=Surabaya&checkin=2021-11-25&checkout=2021-11-26'
response = requests.get(website)
scrapping = BeautifulSoup(response.text, 'html.parser')
items = scrapping.findAll('div', 'card-frame')
for it in items:
    name = it.find('h3', 'title ellipsis')
    print(name)