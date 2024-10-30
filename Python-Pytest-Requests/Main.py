import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '21d0eb123cf85144b63934d4429a2e49'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}

body_pokemonCreate = {
    "name": "generate",
    "photo_id": "-1"
}

body_changeName = {
    "pokemon_id": "119249",
    "name": "NevroticCatNew",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "119249"
}

responseCreate = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemonCreate)

print(responseCreate.text)

responseChange = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changeName)

print(responseChange.text)

responseCatch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_changeName)

print(responseCatch.text)


