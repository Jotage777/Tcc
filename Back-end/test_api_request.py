import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com",
    'X-RapidAPI-Key': "25e38c4f71msh2272423f9de8a61p188799jsnfb0af1f3357d"
    }

conn.request("GET", "/v3/odds/bets", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))