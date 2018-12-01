import sys
import requests
import networkx as nx
from datetime import datetime


clientIdFoursquare = "Y4NEZOZDM5WW23GKXBJWXA524RR4OAETS3500PTNHLS0HEUC"
clientSecretFoursquare = "B2K05PB3QO1VWRCHRRSHHU2E2YW4NILFGRI5UWLE2ALSAPK4"

now = datetime.now()
now = now.date().isoformat()
now = now.replace('-','')


url = "https://api.foursquare.com/v2/venues/explore"

local = input("Digite o local: ")

param = {"client_id": clientIdFoursquare, "client_secret": clientSecretFoursquare,
         "near": local, "v": now, 'limit':10 }

r = requests.get(url = url, params = param)

dados = r.json()
dados = dados['response']['groups'][0]['items']

locais = []

cont = 0
for local in dados:
    print(local['venue']['name'])

    try:
        print(local['venue']['location']['address'])
        print(local['venue']['location']['lat'])
        print(local['venue']['location']['lng'])
        locais.append({'id':cont ,'nome': local['venue']['name'], 'endereco': local['venue']['location']['address']})
        cont = cont + 1
        
    except KeyError as identifier:
        # pass  
        print(local['venue']['location']['lat'])
        print(local['venue']['location']['lng'])

# for lugar in locais:
#     print('\n')
#     print(lugar['id'])
#     print(lugar['nome'])
#     print(lugar['endereco'])

# print(locais)

# print (len(dados))