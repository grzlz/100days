import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

sp.user_playlist_create('12132153305', "Spotipy", public=False)