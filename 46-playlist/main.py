from scraper import get_song_list
from script_spotify import get_uris

user_date = input("Introduce una fecha para iniciar tu viaje musical.")
songs = get_song_list(user_date)

print(get_uris(songs))