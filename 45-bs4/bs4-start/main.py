from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

    print(content)