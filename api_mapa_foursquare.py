import sys
import requests
import networkx as nx
from datetime import datetime
import apiGoogle as G


clientIdFoursquare = "Y4NEZOZDM5WW23GKXBJWXA524RR4OAETS3500PTNHLS0HEUC"
clientSecretFoursquare = "B2K05PB3QO1VWRCHRRSHHU2E2YW4NILFGRI5UWLE2ALSAPK4"
url_foursquare = "https://api.foursquare.com/v2/venues/explore"

now = datetime.now()
now = now.date().isoformat()
now = now.replace('-','')


localDigitado = input("Digite o local: ")

param_foursquare = {"client_id": clientIdFoursquare, "client_secret": clientSecretFoursquare,
         "near": localDigitado, "v": now, 'limit':5 }

r_foursquare = requests.get(url = url_foursquare, params = param_foursquare)

dados_foursquare = r_foursquare.json()
dados_foursquare = dados_foursquare['response']['groups'][0]['items']

locais = []

cont = 0
for local in dados_foursquare:
    localAtual = {'id':cont ,'nome': local['venue']['name'], 'endereco': G.findAddress(local['venue']['location']['lat'],local['venue']['location']['lng']),'distancias': []}
    locais.append(localAtual)
    print('aqui')
    cont = cont + 1
          
  

for lugarAtual in locais:
    for lugar in locais:
        if lugar != lugarAtual:
            origem = lugarAtual['endereco']
            destino = lugar['endereco']

            dist = G.findDistance(origem,destino)

            lugarAtual['distancias'].append({'origem': lugarAtual['id'], 'destino': lugar['id'], 'dist':dist})
            print('la')



for l in locais:
    print(l)
    print("\n")