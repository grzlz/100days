import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read"))
results = sp.current_user_saved_tracks()
user_id = sp.current_user()["id"]

def get_uris(songs):
    uris = []
    for song in songs:
        uris.append(sp.search(song, limit=1).get("tracks").get("items")[0].get("uri"))

    return uris

# print(sp.search("Time pinkfloyd", limit=1).get("tracks").get("items")[0].get("uri"))

""" 
scope = "playlist-modify-private"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


sp.user_playlist_create(user_id, "Spotipy", public=False)

# Next, find 10 songs URIS from scraped list
# Search spotify for the song from step 1 """