from bs4 import BeautifulSoup
import requests
import csv

# array kosong
datas = []
# link website
dokumen = "https://www.kaskus.co.id/"
#cek koneksi
data = requests.get(dokumen)
#scrapping
html_soup = BeautifulSoup(data.text, 'html.parser')
# card scrapping
items = html_soup.findAll('div', 'P(15px) Bd(borderSolidLightGrey) Mb(15px) Bgc(c-white) Pos(r) Ov(h) jsThreadCard')

# loop item for scrapping
for it in items:
    judul = it.find('a', class_='C(c-primary)').text
    genre = it.find('a', class_='C(c-tertiary) Fz(12px)').text

    datas.append([judul, genre])

# title for csv
header = ['Judul', 'Genre']
# write data in csv
convert = csv.writer(open('data/data.csv', 'w', newline=''))
convert.writerow(header)
for d in datas:
    convert.writerow(d)