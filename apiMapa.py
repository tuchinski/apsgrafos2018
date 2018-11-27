import requests


key = "sRXGrXYZZyrnaNM3yGO9AMtx4XroURmp"
url = "http://www.mapquestapi.com/directions/v2/route"

origem = "Rua São Paulo 1486 campo mourão"
destino = "Rua Francisco Abulquerque, 1453 campo mourão"

param = {"key":key, "from": origem, "to": destino, "unit": "k"}

r = requests.get(url = url, params = param)

dados = r.json()

arq = open("json.json", 'w')
arq.write(str(dados))
arq.close()

print(dados['route']['distance'])
