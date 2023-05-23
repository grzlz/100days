import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)