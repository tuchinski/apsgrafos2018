import requests

urlEstados = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

r = requests.get(url=urlEstados)

data = r.json()

estado = input("Digite o nome de um estado: ")

for e in data:
    if e["nome"].lower() == estado.lower():
        print(e)

# print (data)
