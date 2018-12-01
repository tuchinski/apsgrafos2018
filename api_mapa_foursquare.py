import sys
import requests
import networkx as nx
from datetime import datetime


clientIdFoursquare = "Y4NEZOZDM5WW23GKXBJWXA524RR4OAETS3500PTNHLS0HEUC"
clientSecretFoursquare = "B2K05PB3QO1VWRCHRRSHHU2E2YW4NILFGRI5UWLE2ALSAPK4"

keyMapa = "sRXGrXYZZyrnaNM3yGO9AMtx4XroURmp"
urlMapa = "http://www.mapquestapi.com/directions/v2/route"

now = datetime.now()
now = now.date().isoformat()
now = now.replace('-','')


url_foursquare = "https://api.foursquare.com/v2/venues/explore"

localDigitado = input("Digite o local: ")

param_mapa = {"client_id": clientIdFoursquare, "client_secret": clientSecretFoursquare,
         "near": localDigitado, "v": now, 'limit':10 }

r_foursquare = requests.get(url = url_foursquare, params = param_mapa)

dados_foursquare = r_foursquare.json()
dados_foursquare = dados_foursquare['response']['groups'][0]['items']

locais = []

cont = 0
for local in dados_foursquare:
    try:
        localAtual = {'id':cont ,'nome': local['venue']['name'], 'endereco': local['venue']['location']['address'],'distancias': []}
        locais.append(localAtual)
        cont = cont + 1
        
        
    except KeyError as identifier:
        pass

for lugarAtual in locais:
    for lugar in locais:
        if lugar != lugarAtual:
            origem = lugarAtual['endereco'] + " " + localDigitado
            destino = lugar['endereco'] + " " + localDigitado

            param_mapa = {"key":keyMapa, "from": origem, "to": destino, "unit": "k"}
            r_mapa = requests.get(url = urlMapa, params = param_mapa)
            dados = r_mapa.json()
            # print(dados)

            lugarAtual['distancias'].append({'origem': lugarAtual['id'], 'destino': lugar['id'], 'dist':dados['route']['distance']})

for l in locais:
    print(l)
    print("\n")