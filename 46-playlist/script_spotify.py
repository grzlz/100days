import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-currently-playing"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

print(sp.current_user())