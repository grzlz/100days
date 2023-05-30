import requests 
from bs4 import BeautifulSoup

def get_song_list(date):
    site = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/").text
    soup = BeautifulSoup(site, "html.parser")
    songs = soup.select("li ul li h3")
    names = [tag.text.strip() for tag in songs]
    return names