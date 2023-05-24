import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]

sp.user_playlist_create(user_id, "Spotipy", public=False)