import requests 
from bs4 import BeautifulSoup

site = requests.get("https://www.billboard.com/charts/hot-100/2022-06-05/").text
soup = BeautifulSoup(site, "html.parser")
songs = soup.select("li ul li h3")

print(songs[0].text.strip())