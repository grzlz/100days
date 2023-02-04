import requests 

# api_key = "69f04e4613056b159c2761a9d9e664d2"
api_key = "b239ad6816f4e09d41069588e7ac2d80"

# Get Hourly forecast for 48 hours from https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# api_key = "a843491b794fffdf8d6796331a8b6cb1"

parameters = {
    "lat": 21.1743,
    "lon": -86.8466,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params = parameters)

hours = data.json()["hourly"]

climate_id = [hour["weather"][0]["id"] for hour in hours ][:12]
print(climate_id)


# If id < 700 birng umbrella
for i in climate_id:
    if i < 700:
        print("Rainy day")




