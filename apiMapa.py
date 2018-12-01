import requests


keyMapa = "sRXGrXYZZyrnaNM3yGO9AMtx4XroURmp"
urlMapa = "http://www.mapquestapi.com/directions/v2/route"

origem = "Rua São Paulo 1486 campo mourão"
destino = "Rua Francisco Abulquerque, 1453 campo mourão"

param_mapa = {"key":keyMapa, "from": origem, "to": destino, "unit": "k"}

r_mapa = requests.get(url = urlMapa, params = param_mapa)

dados = r_mapa.json()

# arq = open("json.json", 'w')
# arq.write(str(dados))
# arq.close()

print(dados['route']['distance'])
