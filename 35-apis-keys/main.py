import requests 
from twilio.rest import Client

# Twilio setup
account_sid = "AC81f2671430dc9505aaed34057ce8f306"
auth_token = "c9bb14ca91070852e2556e71eac6206d"

# Openweather setup
api_key = "b239ad6816f4e09d41069588e7ac2d80"
parameters = {
    "lat": 21.1743,
    "lon": -86.8466,
    "exclude": "current,minutely,daily",
    "appid": api_key
}
data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params = parameters)
hours = data.json()["hourly"]
climate_id = [hour["weather"][0]["id"] for hour in hours ][:12]


# If id < 700 birng umbrella
raining = False
for i in climate_id:
    if i < 700:
        raining = True
        rainy_day = "rainy day"
        break





if raining:
    # Send text message
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body=f"Remember it's a {rainy_day}.",
                                from_='+14303051259',
                                to='+525548017016'
                            )




