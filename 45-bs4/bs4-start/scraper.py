from bs4 import BeautifulSoup
import requests

# Primero crear código lineal y después hacerlo modular

site = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(site, "html.parser")

movie_tags = soup.find_all(class_ = "title", name = "h3")

movies = [tag.text for tag in movie_tags]

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie} \n")
print(movies)