import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"live":"all"}

headers = {
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "25e38c4f71msh2272423f9de8a61p188799jsnfb0af1f3357d"
}

response = requests.request("GET", url, headers=headers, params=querystring)

responsejson = response.json()
print(json.dumps(responsejson, indent=4, sort_keys=True))