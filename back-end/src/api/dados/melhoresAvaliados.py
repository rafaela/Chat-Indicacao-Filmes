#coding: utf-8
from bs4 import BeautifulSoup
import requests
import re
import json

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find("table", class_=re.compile('chart'))
tbody = table.find("tbody")

filmes = []

for tr in tbody.find_all('tr'):
    filme = {}
    td = tr.find_all("td")
    imagem = td[0].find("a").img.get('src')
    filme['categoria'] = 'Melhores filmes'
    filme['imagem'] = imagem
    filme['titulo'] = tr.find("td", class_=re.compile('titleColumn')).text.replace('\n', '').split(".")[1].strip()
    filme['colocacao'] = tr.find("td", class_=re.compile('titleColumn')).text.replace('\n', '').split(".")[0].strip()
    filme['avaliacao'] = tr.find("td", class_=re.compile('ratingColumn')).text.replace('\n', '').strip()
    
    filmes.append(filme)

with open('melhoresAvaliados.json', 'w') as outfile:

    json.dump(filmes, outfile, indent=4, ensure_ascii=False)