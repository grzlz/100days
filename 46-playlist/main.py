from scraper import get_song_list
from script_spotify import get_uris, create_playlist

user_date = input("Introduce una fecha para iniciar tu viaje musical (formato YYYY-MM-DD): ")
songs = get_song_list(user_date)
uris = get_uris(songs)

if __name__ == "__main__":
    create_playlist(uris)


# TODO incorporate logging
# TODO incorporate year in song search
# TODO I want to see what songs will be added
# TODO incorporate error handling