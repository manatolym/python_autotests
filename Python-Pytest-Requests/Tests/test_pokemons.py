import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '21d0eb123cf85144b63934d4429a2e49'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
TRAINERID = 8291

def test_StatusCode():

 response = requests.get(url = f'{URL}/trainers',params = {'trainer_id': TRAINERID})
 assert response.status_code == 200

def test_TrainerName():

 response_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id': TRAINERID})
 assert response_get.json()["data"][0]["trainer_name"] == 'kotikNevrotik'