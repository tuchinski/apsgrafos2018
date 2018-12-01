import requests

def findAddress(lat, longi):
    urlGoogle = 'https://maps.googleapis.com/maps/api/geocode/json'
    keyG = 'AIzaSyCjtpz6WO-AnbFh-yQl59ZenWLFmTVMZLI'

    latlong = str(lat) + ',' + str(longi)
    param = {'latlng': latlong, 'key': keyG}

    r = requests.get(url = urlGoogle, params = param)
    dados = r.json()
    return dados['results'][0]['formatted_address']

def findDistance(origem, destino):
    url = 'https://maps.googleapis.com/maps/api/directions/json'
    keyG = 'AIzaSyCjtpz6WO-AnbFh-yQl59ZenWLFmTVMZLI'

    param = {'origin': origem, 'destination': destino, 'key': keyG}

    r = requests.get(url=url, params=param)
    dados = r.json()

    return(dados['routes'][0]['legs'][0]['distance']['value'])

    

# print(findDistance('Av. Irmãos Pereira, 2231 - Centro, Campo Mourão - PR, 87300-450', 'Av. Comendador Norberto Marcondes, 733 - Centro, Campo Mourão - PR, 87302-060'))
