import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


scope = "playlist-modify-private"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]

sp.user_playlist_create(user_id, "Spotipy", public=False)

# Next, find 10 songs URIS from scraped list
# Search spotify for the song from step 1