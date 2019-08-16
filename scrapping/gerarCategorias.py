import json
import os


id_categoria = 1
categorias = []

arquivo = 'avaliacaoFilmeGenero.json'
            

def adicionaCategoria(categoria):
    global id_categoria, categorias
    for cat in categorias:
        if cat['nome'] == categoria:
            return cat['id']
    categorias.append({'id': id_categoria, 'nome': categoria})
    id_categoria += 1
    return id_categoria - 1


with open(arquivo, 'r') as jsonFile:
    filmes = json.load(jsonFile)

for j, filme in enumerate(filmes):
    print(filme['genero'])
    generos = [x.strip() for x in filme['genero'].split(',')]
    for i, genero in enumerate(generos):
        generos[i] = adicionaCategoria(genero)
    filmes[j]['genero'] = generos

with open(arquivo, 'w') as outfile:
    json.dump(filmes, outfile, indent=4, ensure_ascii=False)

with open('categorias.json', 'w') as outfile:
    json.dump(categorias, outfile, indent=4, ensure_ascii=False)
    



