import requests
import sys

urlEstados = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
urlCidades = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'

r = requests.get(url=urlCidades)

data = r.json()

cidade = " ".join(sys.argv[1:])

for e in data:
    if e["nome"].lower() == cidade.lower():
        # print(str(e))
        cidade = e
        break
# print (cidade)

try:
        urlMicrorregioes = 'https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes/%s/municipios' % cidade['microrregiao']['id']
except TypeError as identifier:
        print("A cidade não foi encontrada")
        sys.exit(0)

reqMicrorregioes = requests.get(url=urlMicrorregioes)

cidadesMicrorregiao = reqMicrorregioes.json()

for c in cidadesMicrorregiao:
        # c['distancia'] = 100
        print (c['id'])
        print (c['nome'])
        print (c['distancia'])
        print ("\n")
