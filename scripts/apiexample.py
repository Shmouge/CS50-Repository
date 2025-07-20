import requests

#This is a free public API that gives you weather info
url = "https://api.weatherapi.com/v1/current.json"

#You’ll need an API key from https://www.weatherapi.com/
params = {
    "key": "YOUR_API_KEY",
    "q": "Burleson, TX",  #note Location
    "aqi": "no"  #note Air quality info optional
}

response = requests.get(url, params=params)

#Turn it into JSON (like a Python dictionary)
data = response.json()

#Grab specific pieces
location = data["location"]["name"]
temp = data["current"]["temp_f"]
condition = data["current"]["condition"]["text"]

print(f"{location}: {temp}°F and {condition}")