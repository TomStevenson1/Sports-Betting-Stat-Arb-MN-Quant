import requests
import json

api_key = "c8cc9d37d91d92cfe5fb893bb75d9b00"

#Set constants here

BET_SIZE = 100

SPORT = "upcoming"
REGION = "us"
ODDS_FORMAT = 'decimal'
KEY = "basketball_euroleague"



#response = requests.get("https://api.the-odds-api.com/v4/sports?apiKey=c8cc9d37d91d92cfe5fb893bb75d9b00")



response2 = requests.get(f'https://api.the-odds-api.com/v4/sports/{KEY}/odds/?apiKey={api_key}&regions=us&markets=h2h,spreads&oddsFormat=american')


response2.json()

print(response2.text)

print(response2.headers)

print(response2.status_code)



#print(response.json())  # returns literally everything
print(response2.status_code)

