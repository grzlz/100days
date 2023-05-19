from bs4 import BeautifulSoup
import requests

class Scraper():
    def __init__(self, website):
        self.website = website

    def scrape(self):
        website = requests.get(self.website).text
        soup = BeautifulSoup(website, 'html.parser')
        movie_tags = soup.find_all(class_ = "title", name = "h3")
        self.movies = [tag.text for tag in movie_tags][::-1]
    
    def show(self):
        print(self.movies)

    def get_list(self):
        return self.movies

    def write(self, file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            for movie in self.movies:
                file.write(f"{movie} \n")
        print(f"File {file_name} succesfuly created!")









# Primero crear código lineal y después hacerlo modular
""" 
site = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(site, "html.parser")

movie_tags = soup.find_all(class_ = "title", name = "h3")

movies = [tag.text for tag in movie_tags][::-1]

# Reverse the order of the list


with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie} \n")
print(movies) """