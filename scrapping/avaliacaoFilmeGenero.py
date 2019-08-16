#coding: utf-8
from bs4 import BeautifulSoup
import requests
import re
import json

urls = ['https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=FJMTZ55WRTX58HWJHG5A&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1',
        'https://www.imdb.com/search/title/?genres=animation&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_3',
        'https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2',
        'https://www.imdb.com/search/title/?genres=biography&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_4',
        'https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_5',
        'https://www.imdb.com/search/title/?genres=crime&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_6',
        'https://www.imdb.com/search/title/?genres=drama&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_7',
        'https://www.imdb.com/search/title/?genres=sport&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_18',
        'https://www.imdb.com/search/title/?genres=family&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_8',
        'https://www.imdb.com/search/title/?genres=fantasy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_9',
        'https://www.imdb.com/search/title/?genres=film_noir&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_10',
        'https://www.imdb.com/search/title/?genres=war&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_20',
        'https://www.imdb.com/search/title/?genres=history&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_11',
        'https://www.imdb.com/search/title/?genres=mystery&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_15',
        'https://www.imdb.com/search/title/?genres=music&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_13',
        'https://www.imdb.com/search/title/?genres=musical&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_14',
        'https://www.imdb.com/search/title/?genres=western&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_21',
        'https://www.imdb.com/search/title/?genres=romance&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16',
        'https://www.imdb.com/search/title/?genres=sci_fi&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_17',
        'https://www.imdb.com/search/title/?genres=horror&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_12',
        'https://www.imdb.com/search/title/?genres=thriller&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=ZZVQ9VGDF5QMR5T56DS3&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_19']
i = 0

filmes = []
for url in urls:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    div = soup.find_all("div", class_=re.compile('lister-list'))

    
    for lista in div:
        item = lista.find_all("div", class_=re.compile('lister-item'))
        for film in item:
            filme = {}
            filme['categoria'] = 'Melhores filmes por gênero'
            imagem = item[0].find_all("a")[0]
            filme['imagem'] = imagem.img.get('loadlate')
            
            titulo = film.find("a").text.strip()
            if titulo != "":
                filme['titulo'] = titulo
                
                ano = film.find("span", class_=re.compile('lister-item-year'))
                if ano == None:
                    filme['ano'] = 'Não informado'
                else:
                    filme['ano'] = ano.text.strip()
                
                classificacao = film.find("span", class_=re.compile('certificate'))
                if classificacao == None:
                    filme['classificacao'] = 'Não informado'
                else:
                    filme['classificacao'] = classificacao.text.strip()
                
                duracao = film.find("span", class_=re.compile('runtime'))
                if duracao == None:
                    filme['duracao'] = 'Não informado'
                else:
                    filme['duracao'] = duracao.text.strip()
                
                genero = film.find("span", class_=re.compile('genre'))
                if genero == None:
                    filme['genero'] =  'Não informado'
                else:
                    filme['genero'] =  genero.text.strip()

                
                nota = film.find("strong")
                if nota == None:
                    filme['avaliacao'] =  'Não informado'
                else:
                    filme['avaliacao'] =  nota.text.strip()
                
                resumo = film.find_all("p", class_=re.compile('text-muted'))
                if len(resumo) > 1:
                    filme['resumo'] = resumo[1].text.strip()

                diretor = film.find_all("p", class_=re.compile(''))
                if len(diretor) > 2:
                    filme['diretor'] = diretor[2].a.text.strip()
                
                ator = film.find_all("p", class_=re.compile(''))
                elenco = []
                if len(ator) > 2:
                    atores = ator[2].find_all("a")
                    for ator in atores[1:]:
                        elenco.append(ator.text.strip())

                filme['elenco'] = elenco
                
                filmes.append(filme)

    
with open('avaliacaoFilmeGenero.json', 'w') as outfile:
    json.dump(filmes, outfile, indent=4, ensure_ascii=False)