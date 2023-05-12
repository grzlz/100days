import requests 
from bs4 import BeautifulSoup

site = requests.get("https://www.billboard.com/charts/hot-100/2022-06-05/").text
soup = BeautifulSoup(site, "html.parser")
print(soup)