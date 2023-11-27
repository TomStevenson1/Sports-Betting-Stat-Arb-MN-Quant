import requests

api_key = "c8cc9d37d91d92cfe5fb893bb75d9b00"

# Construct the URL with the API key as a query parameter


response = requests.get("https://api.the-odds-api.com/v4/sports?apiKey=c8cc9d37d91d92cfe5fb893bb75d9b00")
print(response.json())  # returns literally everything
print(response.status_code)
