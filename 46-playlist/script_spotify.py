import os
import spotipy
from json import dumps
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))
user_id = sp.current_user()["id"]
def get_uris(songs):
    uris = []
    i = 1
    for song in songs:
        print(i, song)
        try:
            uris.append(sp.search(f"{song}", limit=1).get("tracks").get("items")[0].get("uri"))
        except:
            print(f"{song} does not exist in Spotify.")
        i += 1
    return uris

def create_playlist(uris):
    playlist_id = sp.user_playlist_create(user_id, "Spotipy Billboard", public=False).get("id")
    sp.playlist_add_items(playlist_id=playlist_id, items= uris)
