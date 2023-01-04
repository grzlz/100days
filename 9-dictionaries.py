# Travel log

travel_log = [
    {
    "country_visited": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {
    "country_visited": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 16
    }
]

# Write a function that will add a new country to the list

def add_new_country(country_name, cities_name, visits):
    new_country = {
        "country_visited": country_name,
        "cities_visited": cities_name,
        "total_visits": visits
    }

    travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "SP"], 3)

print(travel_log)