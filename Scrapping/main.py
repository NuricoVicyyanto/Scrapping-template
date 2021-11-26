from bs4 import BeautifulSoup
import requests
import csv

datas = []
dokumen = "https://www.kaskus.co.id/"
data = requests.get(dokumen)
html_soup = BeautifulSoup(data.text, 'html.parser')
items = html_soup.findAll('div', 'P(15px) Bd(borderSolidLightGrey) Mb(15px) Bgc(c-white) Pos(r) Ov(h) jsThreadCard')
for it in items:
    judul = it.find('a', class_='C(c-primary)').text
    genre = it.find('a', class_='C(c-tertiary) Fz(12px)').text

    datas.append([judul, genre])

header = ['Judul', 'Genre']
convert = csv.writer(open('data/data.csv', 'w', newline=''))
convert.writerow(header)

for d in datas:
    convert.writerow(d)